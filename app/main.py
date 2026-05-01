from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_engine import detect_intent
from app.automation import generate_response

app = FastAPI()

class Query(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Support Bot Running"}

@app.post("/chat")
def chat(query: Query):
    intent = detect_intent(query.message)
    response = generate_response(intent, query.message)

    return {
        "intent": intent,
        "response": response
    }
