from pydantic import BaseModel
from typing import List, Optional


class GenerateRequest(BaseModel):
    query: str


class Match(BaseModel):
    docId: str
    title: str
    score: float
    text: str


class GenerateResponse(BaseModel):
    query: str
    summary: str
    matches: List[Match]

