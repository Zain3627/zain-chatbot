# RAG Knowledge Base Chatbot

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot that answers questions over a custom knowledge base using **Hybrid Search** (BM25 + Dense Retrieval). The system combines lexical and semantic retrieval to improve answer relevance before generating grounded responses with a Large Language Model through a FastAPI backend.

## Features

- 🤖 Retrieval-Augmented Generation (RAG)
- 🔍 Hybrid Search using **BM25** and **FAISS** vector search
- 🧠 Semantic embeddings with **all-MiniLM-L6-v2**
- 📄 Markdown-aware document chunking
- ⚡ FastAPI REST API
- 🐳 Dockerized for deployment
- ☁️ Deployable on AWS EC2
- 📊 LangSmith tracing for observability
- 🚀 Cached pipeline for low-latency inference

---

# Architecture

```
                    Markdown Knowledge Base
                              │
                              ▼
                     Markdown Loader
                              │
                              ▼
              Markdown Header Text Splitter
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
      HuggingFace Embeddings          BM25 Index
      (all-MiniLM-L6-v2)                 │
                 │                       │
                 ▼                       ▼
            FAISS Vector Store      Keyword Search
                 │                       │
                 └────────────┬──────────┘
                              ▼
                    Ensemble Retriever
                   (Hybrid Search)
                              │
                     Top Relevant Chunks
                              │
                              ▼
              Prompt + Retrieved Context
                              │
                              ▼
                     Google Gemma 4
                              │
                              ▼
                      Generated Answer
```

---

# Tech Stack

### AI & LLM

- LangChain
- Google Gemma 4
- HuggingFace Embeddings
- Retrieval-Augmented Generation (RAG)

### Retrieval

- FAISS
- BM25
- Ensemble Retriever (Hybrid Search)

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Monitoring

- LangSmith

### Deployment

- Docker
- AWS EC2

---

# Project Structure

```
.
├── raw-files/
│   └── zain-tamer-knowledge-base.md
├── main.py
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

# Pipeline

## 1. Load Knowledge Base

The chatbot loads a Markdown knowledge base.

```
TextLoader
```

---

## 2. Split Documents

The document is divided according to Markdown headers (`#`, `##`, `###`) to preserve document structure and improve retrieval quality.

---

## 3. Build Retrieval Indexes

### Dense Retrieval

Each chunk is embedded using

```
all-MiniLM-L6-v2
```

and stored in a **FAISS vector database** for semantic similarity search.

### Lexical Retrieval

A **BM25** index is created over the same document chunks to capture exact keyword matches.

---

## 4. Hybrid Search

Instead of relying on a single retrieval strategy, the chatbot combines both retrievers using LangChain's `EnsembleRetriever`.

```python
EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.5, 0.5]
)
```

This approach improves retrieval performance by combining:

- **Dense Retrieval (FAISS)** for semantic understanding
- **BM25** for exact keyword matching

Hybrid retrieval generally produces more relevant context, especially for technical terms, names, abbreviations, and natural-language questions.

---

## 5. Context Generation

The top retrieved chunks are merged into a single context block.

```
Top BM25 Results
        +
Top Semantic Results
        ↓
Merged Context
```

---

## 6. Response Generation

The retrieved context is passed to the LLM with the prompt:

> Use ONLY the context below to answer. If the answer isn't in the context, say you don't know.

This ensures grounded responses and reduces hallucinations.

---

# API

## POST `/ask`

Ask a question about the knowledge base.

### Request

```json
{
    "question": "Who is Zain Tamer?"
}
```

### Response

```json
{
    "answer": "..."
}
```

---

# Running Locally

## Clone

```bash
git clone https://github.com/Zain3627/<repository-name>.git
cd <repository-name>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
LANGSMITH_API_KEY=YOUR_API_KEY
```

---

## Run

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

Open

```
http://localhost:8000/docs
```

to access the Swagger UI.

---

# Docker

Build the image

```bash
docker build -t rag-chatbot .
```

Run the container

```bash
docker run -p 8000:8000 --env-file .env rag-chatbot
```

---

# Deployment

The application is deployed as a Docker container on an AWS EC2 instance.

Deployment stack:

- Docker
- FastAPI
- AWS EC2
- REST API
- CORS-enabled frontend integration

---

# Performance Optimizations

- Pipeline initialized once during FastAPI startup
- `lru_cache()` prevents rebuilding the retrieval pipeline
- FAISS enables fast approximate nearest-neighbor search
- BM25 improves keyword retrieval
- Hybrid Search balances semantic similarity and lexical matching
- Markdown-aware chunking preserves document hierarchy

---

# Future Improvements

- Persistent FAISS index (avoid rebuilding on startup)
- Streaming responses
- Multi-document ingestion
- Metadata filtering
- Cross-Encoder reranking
- Conversation memory
- User authentication
- Rate limiting
- Evaluation pipeline with retrieval metrics

---

# Example

### Question

```
What machine learning projects has Zain worked on?
```

### Retrieval

Hybrid Search retrieves:

- Relevant semantic matches from FAISS
- Relevant keyword matches from BM25

↓

Merged context is supplied to Gemma 4.

↓

Grounded answer is returned to the user.

---

# Author

- **Zain Tamer**
- **ChatGPT**
Machine Learning Engineer | MLOps Engineer | LLM & RAG Enthusiast

- GitHub: https://github.com/Zain3627
- Portfolio: https://zaintamer.vercel.app