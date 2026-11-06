import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class ShawarmaBrain:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is missing!")
        self.client = Groq(api_key=api_key)

    def generate_response(self, prompt: str, mode: str = "general") -> str:
        system_instruction = "You are Shawarma AI, a highly versatile AI assistant."
        
        if mode == "medical_music":
            system_instruction += (
                " You specialize in medical music therapy, acoustic signal analysis, "
                "binaural beat frequencies, and sound-driven health interventions."
            )

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
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
        zone = "Alpha (8-12 Hz) - Deep Relaxation" if frequency_hz <= 12 else "Beta (13-30 Hz) - Active Focus"
        return {
            "status": "ready",
            "frequency_hz": frequency_hz,
            "therapeutic_zone": zone
        }