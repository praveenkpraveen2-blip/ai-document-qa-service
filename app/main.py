from fastapi import FastAPI
from app.api import documents, search, qa

app = FastAPI(title="AI Document QA Service")

# Register routers
app.include_router(documents.router)
app.include_router(search.router)
app.include_router(qa.router)