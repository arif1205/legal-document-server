from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data.legal_docs.documents import DOCS
from models.schemas import GenerateRequest, GenerateResponse, Match
from utils.helpers import keywords, score, make_summary

app = FastAPI(title="Legal documents mock API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    fetched_keywords = keywords(req.query)
    scored = []
    
    for d in DOCS:
        sc = score(d["text"], fetched_keywords)
        # If score is not 0 then, add to the matched list
        if sc > 0:
            trimmed_text = ''
            if len(d["text"]) > 200:
                trimmed_text = d["text"][:200] + "..."
            else:
                trimmed_text = d["text"]

            scored.append(
                Match(
                    docId=d["id"],
                    title=d["title"],
                    score=round(sc / 10.0, 2),
                    text=trimmed_text,
                )
            )

    # Sort according to the higher score first
    scored.sort(key=lambda m: m.score, reverse=True)
    # This is just the demo summary with the first scored text
    summary = make_summary(scored)

    return GenerateResponse(
        query=req.query,
        summary=summary,
        matches=scored[:3],
        
    )
