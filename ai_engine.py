import os
from typing import List, Dict
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class ShawarmaBrain:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing")
            
        self.client = genai.Client(api_key=api_key)

    def generate_response(
        self, 
        prompt: str, 
        mode: str = "general", 
        history: List[Dict[str, str]] = None
    ) -> str:
        system_instruction = "You are Shawarma AI, a highly versatile AI assistant."
        
        if mode == "medical_music":
            system_instruction += (
                " You specialize in medical music therapy, acoustic signals, "
                "binaural beat frequencies, and sound-driven health interventions."
            )

        contents = []
        if history:
            for msg in history:
                role = "user" if msg["role"] == "user" else "model"
                contents.append(
                    types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=msg["content"])]
                    )
                )

        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)]
            )
        )

        response = self.client.models.generate_content(
            model="gemini-3.8-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
            )
        )
        return response.text

class MedicalMusicEngine:
    @staticmethod
    def analyze_tone(frequency_hz: float):
        zone = "Alpha (8-12 Hz) - Deep Relaxation" if frequency_hz <= 12 else "Beta (12+ Hz) - Alertness"
        return {
            "status": "ready",
            "frequency_hz": frequency_hz,
            "therapeutic_zone": zone
        }