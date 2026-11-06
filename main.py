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

class ChatRequest(BaseModel):
    prompt: str
    mode: str = "general"

@app.get("/")
def root():
    return {"status": "Shawarma AI Engine Active", "stack": "Python + FastAPI"}

@app.post("/api/chat")
def chat(request: ChatRequest):
    try:
        reply = brain.generate_response(request.prompt, request.mode)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/music-health/{freq}")
def music_health(freq: float):
    return MedicalMusicEngine.analyze_tone(freq)