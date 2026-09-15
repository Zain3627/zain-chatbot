from collections.abc import Sequence
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from functools import lru_cache
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ← ADD THIS
from pydantic import BaseModel, Field
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers.ensemble import EnsembleRetriever

load_dotenv()
MAX_HISTORY_MESSAGES = 3
MAX_HISTORY_CONTENT_CHARS = 400
MAX_RETRIEVAL_HISTORY_CHARS = 180

file_paths = [
    "raw-files/arabic-egypt-zain-tamer-knowledge-base.md",
    "raw-files/arabic-zain-tamer-knowledge-base.md",
    "raw-files/english-zain-tamer-knowledge-base.md",
    "raw-files/franco-arabic-zain-tamer-knowledge-base.md",
]


class ConversationMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1)


class QuestionRequest(BaseModel):
    question: str
    history: list[ConversationMessage] = Field(default_factory=list)


class AnswerResponse(BaseModel):
    answer: str


# RAG pipeline methods

def document_loader():
    all_docs = []
    for path in file_paths:
        loader = TextLoader(path, encoding="utf-8")
        all_docs.extend(loader.load())
    return all_docs

def chunk_docs(docs):
    headers_to_split_on = [
        ("#",   "header"),
        ("##",  "section"),
        ("###", "subsection"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    all_chunks = []
    for doc in docs:                                    # ← iterate all docs now
        chunks = markdown_splitter.split_text(doc.page_content)
        all_chunks.extend(chunks)
    return all_chunks

def wrap_retriever(split_docs):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    bm25_retriever = BM25Retriever.from_documents(split_docs)
    bm25_retriever.k = 5

    retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, dense_retriever],
        weights=[0.5, 0.5]   # tune: raise BM25 weight for keyword-heavy queries
    )

    return retriever

def initialize_model():
    prompt = ChatPromptTemplate.from_template("""
    You are a personal assistant that answers questions about Zain Tamer. You can answer with that if you are asked about who you are.
    Use ONLY the context below to answer. If the answer isn't in the context, say you don't know.

    Use the recent conversation only to understand references and follow-up questions.

    Recent conversation (up to three messages):
    {history}

    Context:
    {context}

    Question:
    {question}
""")
    model = init_chat_model(
        "google_genai:gemma-4-26b-a4b-it",
        temperature=1.0,
        thinking_level="minimal",
    )
    return prompt, model

def merge_selected_chunks(docs):
    docs = docs[:6]
    return "\n\n".join(
        f"[{d.metadata.get('subsection', '')}]\n{d.page_content}"
        for d in docs
    )


def format_history(history: Sequence[ConversationMessage] | None) -> str:
    if not history:
        return "No previous messages."

    return "\n".join(
        f"{message.role.capitalize()}: {message.content[:MAX_HISTORY_CONTENT_CHARS]}"
        for message in history[-MAX_HISTORY_MESSAGES:]
    )


def retrieval_question(question: str, history: Sequence[ConversationMessage] | None) -> str:
    # Previous assistant answers can be long and contain terms unrelated to the
    # follow-up. The last user question supplies the topic with a small bound.
    last_user_question = next(
        (message.content for message in reversed(history or []) if message.role == "user"),
        None,
    )
    if last_user_question:
        return f"{last_user_question[:MAX_RETRIEVAL_HISTORY_CHARS]}\n{question}"
    return question


@lru_cache(maxsize=1)
def build_rag_pipeline():
    docs = document_loader()
    split_docs = chunk_docs(docs) 
    retriever = wrap_retriever(split_docs)
    prompt, model = initialize_model()
    return prompt, model, retriever

@traceable(name="zain-chatbot")
def run_chain(
    prompt,
    model,
    retriever,
    question: str,
    history: Sequence[ConversationMessage] | None = None,
) -> str:
    history_text = format_history(history)
    retrieval_query = retrieval_question(question, history)
    context = merge_selected_chunks(retriever.invoke(retrieval_query))
    prompt_value = prompt.invoke(
        {"context": context, "history": history_text, "question": question}
    )
    return StrOutputParser().invoke(model.invoke(prompt_value))


def answer_question(
    question: str,
    history: Sequence[ConversationMessage | dict[str, str]] | None = None,
) -> str:
    parsed_history = [
        message
        if isinstance(message, ConversationMessage)
        else ConversationMessage.model_validate(message)
        for message in (history or [])
    ]
    prompt, model, retriever = build_rag_pipeline()
    return run_chain(prompt, model, retriever, question, parsed_history)


# start FastAPI lifespan

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Building RAG pipeline …")
    build_rag_pipeline()
    print("RAG pipeline ready.")
    yield

app = FastAPI(title="Zain Tamer Chatbot", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://zaintamer.vercel.app",
        "https://zain3627.github.io",       
        "http://localhost:5173",            
        "http://localhost:4173",            
    ],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

# Endpoint

@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    """
    Send a question and get an answer from the RAG pipeline.

    Body: {
        "question": "What did he build it with?",
        "history": [
            {"role": "user", "content": "Tell me about Zain's latest project."}
        ]
    }
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question must not be empty.")

    answer = answer_question(request.question, request.history)
    return AnswerResponse(answer=answer)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
