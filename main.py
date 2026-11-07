import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from ai_engine import ShawarmaBrain

app = FastAPI(title="Shawarma AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

brain = ShawarmaBrain()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    prompt: str
    mode: str = "general"
    history: Optional[List[Message]] = []

@app.post("/api/chat")
def chat(request: ChatRequest):
    try:
        reply = brain.generate_response(
            prompt=request.prompt,
            mode=request.mode,
            history=[m.model_dump() for m in request.history] if request.history else []
        )
        return {"response": reply}
    except Exception as e:
        print("\n=== FULL ERROR TRACEBACK ===")
        traceback.print_exc()
        print("============================\n")
        raise HTTPException(status_code=500, detail=str(e))