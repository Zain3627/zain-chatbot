from dotenv import load_dotenv
from functools import lru_cache
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

load_dotenv()
file_path = "raw-files/zain-tamer-knowledge-base.md"

def test_inference(input_text : str):
    model = init_chat_model("google_genai:gemma-4-26b-a4b-it", 
                            temperature=0.2,
                            )
    response = model.invoke(input_text)
    return response.text()

def document_loader():
    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()
    
    return docs

def chunk_docs(docs):
    headers_to_split_on = [
    ("#", "header"),
    ("##", "section"),      
    ("###", "subsection"),  
]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    split_docs = markdown_splitter.split_text(docs) 
    return split_docs

def wrap_retriever(split_docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    return retriever

def initialize_model():
    prompt = ChatPromptTemplate.from_template("""
    You are a personal assistant that answers questions about Zain Tamer.
    Use ONLY the context below to answer. If the answer isn't in the context, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """)
    model = init_chat_model("google_genai:gemma-4-26b-a4b-it", 
                                temperature=1.0,
                                )
    return prompt, model

def merge_selected_chunks(docs):
    return "\n\n".join(
        f"[{d.metadata.get('subsection', '')}]\n{d.page_content}"
        for d in docs
    )


@lru_cache(maxsize=1)
def build_rag_pipeline():
    docs = document_loader()
    split_docs = chunk_docs(docs[0].page_content)
    retriever = wrap_retriever(split_docs)
    prompt, model = initialize_model()
    return prompt, model, retriever

@traceable(name="zain-chatbot")
def chain(prompt, model, retriever, question):
    chain = (
        {"context": retriever | merge_selected_chunks, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    response = chain.invoke(question)
    return response


def answer_question(question: str):
    prompt, model, retriever = build_rag_pipeline()
    return chain(prompt, model, retriever, question)


if __name__ == "__main__":
    response = answer_question("What projects has Zain built in ml field?")
    print(response)