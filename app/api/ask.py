from fastapi import APIRouter
from app.schemas.ask import AskRequest, AskResponse
from app.search.duckduckgo import DuckDuckGoSearchProvider
from app.ai.llm import generate_answer

router = APIRouter(prefix="/", tags=["Ask"])

@router.post("ask", response_model=AskResponse)
def ask(data: AskRequest):
    searcher = DuckDuckGoSearchProvider()
    results = searcher.search(data.query)

    answer = generate_answer(data.query, results)

    return { "answer": answer, "sources": [r["url"] for r in results] }
