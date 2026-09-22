from config import get_llm_response

def run_chatbot(question: str) -> str:
    """
    Plain chatbot: makes one LLM call with no access to any private files.
    """
    system_msg = "You are a study assistant. Answer the user's questions to the best of your general knowledge."
    response = get_llm_response(question, system_message=system_msg)
    return response

if __name__ == "__main__":
    q = "What's due this week?"
    print(f"User: {q}")
    print(f"Chatbot: {run_chatbot(q)}")
