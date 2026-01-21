from fastapi import APIRouter
from app.models.schemas import Question
from app.services.elasticsearch_service import search_documents
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/qa", tags=["QA"])

@router.post("")
def answer_question(q: Question):
    """
    Answers a question using Retrieval-Augmented Generation (RAG).
    """
    docs = search_documents(q.question)

    if not docs:
        return {"answer": "I don't know", "sources": []}

    context = " ".join([doc["text"] for doc in docs])
    answer = generate_answer(context, q.question)

    return {
        "answer": answer,
        "sources": docs
    }
