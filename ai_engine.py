import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ShawarmaBrain:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing")
            
        # Google AI Studio's free OpenAI-compatible endpoint
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def generate_response(self, prompt: str, mode: str = "general") -> str:
        system_instruction = "You are Shawarma AI, a highly versatile AI assistant."
        
        if mode == "medical_music":
            system_instruction += (
                " You specialize in medical music therapy, acoustic signals, "
                "binaural beat frequencies, and sound-driven health interventions."
            )

        completion = self.client.chat.completions.create(
            model="gemini-3.8-flash",  # Updated active free-tier model identifier for Google AI Studio
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content

class MedicalMusicEngine:
    @staticmethod
    def analyze_tone(frequency_hz: float):
        zone = "Alpha (8-12 Hz) - Deep Relaxation" if frequency_hz <= 12 else "Beta (12+ Hz) - Alertness"
        return {
            "status": "ready",
            "frequency_hz": frequency_hz,
            "therapeutic_zone": zone
        }