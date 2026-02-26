from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Enterprise RAG Assistant")


class Query(BaseModel):
    question: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/query")
async def query(q: Query):
    # Placeholder: wire up vector DB retriever + LLM inference here.
    # Return a minimal stub while integrating your RAG pipeline.
    return {
        "question": q.question,
        "answer": "This is a stub response. Integrate RAG pipeline here."
    }
