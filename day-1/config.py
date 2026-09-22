import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client using Groq's base URL
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("MODEL", "llama3-70b-8192")

def get_llm_response(prompt: str, system_message: str = "You are a helpful AI assistant.") -> str:
    """Helper to make a simple LLM call."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content
