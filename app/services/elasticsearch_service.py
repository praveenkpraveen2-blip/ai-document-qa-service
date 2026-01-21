from elasticsearch import Elasticsearch

INDEX_NAME = "documents"

# Elasticsearch client
es = Elasticsearch("http://localhost:9200")

def index_document(doc_id: str, text: str, metadata: dict):
    """
    Indexes a document for full-text search.
    """
    body = {
        "text": text,
        "metadata": metadata
    }
    es.index(index=INDEX_NAME, id=doc_id, document=body)

def search_documents(query: str, size: int = 3):
    """
    Searches documents using Elasticsearch full-text search.
    """
    body = {
        "query": {
            "match": {
                "text": query
            }
        }
    }
    response = es.search(index=INDEX_NAME, body=body, size=size)
    return [hit["_source"] for hit in response["hits"]["hits"]]
