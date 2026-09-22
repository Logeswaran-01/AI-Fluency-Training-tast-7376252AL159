import sys
import os
from dotenv import load_dotenv

def check_environment():
    print("Checking setup...")
    
    # Check Python version
    print(f"Python version: {sys.version.split(' ')[0]}")
    
    # Check for .env file
    if os.path.exists(".env"):
        print(".env file found.")
        load_dotenv()
        if os.getenv("GROQ_API_KEY"):
            print("GROQ_API_KEY is configured.")
        else:
            print("WARNING: GROQ_API_KEY is not set in .env")
    else:
        print("WARNING: .env file not found.")
        
    print("Setup check complete.")

if __name__ == "__main__":
    check_environment()
