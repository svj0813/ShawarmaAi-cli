from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import ShawarmaBrain, MedicalMusicEngine

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

@app.get("/")
def root():
    return {"status": "Shawarma AI Engine Active", "stack": "Python + FastAPI"}

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
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/music-health/{freq}")
def music_health(freq: float):
    return MedicalMusicEngine.analyze_tone(freq)