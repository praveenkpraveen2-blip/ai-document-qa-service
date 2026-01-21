# AI Document QA Service

This project demonstrates a simple AI-powered document ingestion, search,
and question-answering service using FastAPI.

## Architecture
- FastAPI for API orchestration
- Elasticsearch for document retrieval
- LLM (mocked) for answer generation

## Key Concepts
- Clean separation of concerns
- Retrieval-Augmented Generation (RAG)
- Production-oriented design

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
