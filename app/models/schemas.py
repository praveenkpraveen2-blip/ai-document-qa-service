from pydantic import BaseModel
from typing import Dict, Optional

class Document(BaseModel):
    id: str
    text: str
    metadata: Optional[Dict] = {}

class Question(BaseModel):
    question: str