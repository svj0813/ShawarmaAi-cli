import sys
import requests

API_URL = "http://127.0.0.1:8000/api/chat"

def main():
    print("🌯 ShawarmaAI CLI Initialized! Type 'exit' to quit.\n")
    
    while True:
        try:
            prompt = input("You: ")
            if prompt.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            if not prompt.strip():
                continue
                
            response = requests.post(
                API_URL,
                json={"prompt": prompt, "mode": "general"}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"\nShawarmaAI: {data.get('response')}\n")
            else:
                print(f"\n[Error {response.status_code}]: {response.text}\n")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except requests.exceptions.ConnectionError:
            print("\n[Error]: Could not connect to FastAPI server. Is uvicorn running?\n")
            break

if __name__ == "__main__":
    main()