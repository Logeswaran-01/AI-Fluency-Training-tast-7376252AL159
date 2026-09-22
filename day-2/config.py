"""Shared configuration: chooses the LLM provider and holds the lab data."""
import os
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()  # reads the .env file in this folder
 
PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()
 
if PROVIDER == "ollama":                      # Option A: local model, no key
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"                        # any text works for Ollama
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")
elif PROVIDER == "groq":                      # Option B: free cloud key
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
elif PROVIDER == "huggingface":               # Option C: free cloud key
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
else:
    raise SystemExit(f"Unknown PROVIDER '{PROVIDER}'. Use ollama, groq or huggingface.")
 
if not API_KEY:
    raise SystemExit(f"No API key found for PROVIDER={PROVIDER}. Check your .env file.")
 
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
 
# Trip-planning data for a 5-day Goa trip (all prices in Rs.)
TRIP_PRICES = {"FLIGHT": 9200, "HOTEL_3STAR": 7600, "HOTEL_4STAR": 11000, "SCUBA": 3500}

QUESTIONS = [
    "What is the price of the HOTEL_4STAR package?",
    "What is the total cost for FLIGHT and HOTEL_3STAR after a 5% booking convenience fee?",
    "Is HOTEL_4STAR more expensive than HOTEL_3STAR, and by how much?",
    "Write a two-line welcome message for someone planning a Goa trip.",
]
 
def banner(system_name):
    print(f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n")