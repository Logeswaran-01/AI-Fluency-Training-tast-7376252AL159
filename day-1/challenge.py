import sys
from chatbot import run_chatbot
from workflow import run_workflow
from agent import run_agent

QUESTIONS = [
    "Name the subject with the most pending hours.",
    "Do I have any classes scheduled on Friday?",
    "What is my weakest topic in the study log?",
    "List only the names of the pending assignments."
]

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print("=== Private Study and Deadline Assistant ===\n")
    
    for i, q in enumerate(QUESTIONS, 1):
        print(f"--- QUESTION {i}: {q} ---\n")
        
        print("1. PLAIN CHATBOT")
        try:
            chatbot_resp = run_chatbot(q)
            print(chatbot_resp + "\n")
        except Exception as e:
            print(f"Error: {e}\n")
            
        print("2. RULE-BASED WORKFLOW")
        try:
            workflow_resp = run_workflow(q)
            print(workflow_resp + "\n")
        except Exception as e:
            print(f"Error: {e}\n")
            
        print("3. AI AGENT (LLM + Tools + Loop)")
        try:
            agent_resp = run_agent(q)
            print(agent_resp + "\n")
        except Exception as e:
            print(f"Error: {e}\n")
        
        print("="*50 + "\n")

    print("Done!")

if __name__ == "__main__":
    main()
