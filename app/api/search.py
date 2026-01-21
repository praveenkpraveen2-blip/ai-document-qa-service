from fastapi import APIRouter
from app.services.elasticsearch_service import search_documents

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("")
def search(query: str):
    """
    Searches indexed documents.
    """
    results = search_documents(query)
    return {"results": results}
