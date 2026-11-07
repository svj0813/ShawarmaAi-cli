import sys
import requests

API_URL = "http://127.0.0.1:8000/api/chat"

def main():
    print("🌯 ShawarmaAI CLI Initialized (Memory Enabled)! Type 'exit' to quit.\n", flush=True)
    history = []
    
    while True:
        try:
            prompt = input("You: ").strip()
            
            if prompt.lower() in ["exit", "quit"]:
                print("Goodbye!", flush=True)
                break
            if not prompt:
                continue
                
            payload = {
                "prompt": prompt,
                "mode": "general",
                "history": history
            }
            
            response = requests.post(API_URL, json=payload, timeout=15)
            
            if response.status_code == 200:
                reply = response.json().get("response", "")
                print(f"\nShawarmaAI: {reply}\n", flush=True)
                
                history.append({"role": "user", "content": prompt})
                history.append({"role": "assistant", "content": reply})
            else:
                print(f"\n[Error {response.status_code}]: {response.text}\n", flush=True)
                
        except KeyboardInterrupt:
            print("\nGoodbye!", flush=True)
            sys.exit(0)
        except requests.exceptions.Timeout:
            print("\n[Error]: Request timed out. Gemini API took too long to respond.\n", flush=True)
        except requests.exceptions.ConnectionError:
            print("\n[Error]: Could not connect to FastAPI server. Is uvicorn running?\n", flush=True)
            break

if __name__ == "__main__":
    main()