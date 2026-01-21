from fastapi import APIRouter, HTTPException
from app.models.schemas import Document
from app.services.elasticsearch_service import index_document

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("")
def ingest_document(doc: Document):
    """
    Ingests and indexes a document.
    """
    try:
        index_document(doc.id, doc.text, doc.metadata)
        return {"message": "Document indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
