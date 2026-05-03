from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_engine import detect_intent
from app.automation import generate_response
import requests  # add this

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

    # Zapier webhook call (REAL integration)
    try:
        requests.post(
            "https://hooks.zapier.com/hooks/catch/27370622/uvcoqhf/",  # zapier URL
            json={
                "message": query.message,
                "intent": intent,
                "response": response
            },
            timeout=5
        )
    except Exception as e:
        print("Zapier error:", e)  # API crash nahi thase

    return {
        "intent": intent,
        "response": response
    }