from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.router import LLMRouter
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Agent Platform")
router = LLMRouter()

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: QueryRequest):
    result = router.route(request.query)
    return result
