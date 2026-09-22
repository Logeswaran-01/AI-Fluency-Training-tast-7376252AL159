import json
from config import client, MODEL
from tools import TOOLS, AVAILABLE_FUNCTIONS

def run_agent(question: str, max_iterations=5) -> str:
    """
    AI Agent: LLM + Tools + Loop
    It decides which tools to call, executes them, and loops until it answers the question.
    """
    messages = [
        {"role": "system", "content": "You are an intelligent study assistant. You have access to tools to read the user's assignments, timetable, and study log. Use these tools to answer their questions accurately. Do not make up information without querying the tools first."},
        {"role": "user", "content": question}
    ]
    
    for _ in range(max_iterations):
        # 1. Reason & Decide Action
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.0
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)
        
        # 2. Check if a tool needs to be called
        tool_calls = response_message.tool_calls
        if tool_calls:
            # 3. Act & Observe
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = AVAILABLE_FUNCTIONS.get(function_name)
                
                if function_to_call:
                    function_response = function_to_call()
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                else:
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": "Function not found.",
                        }
                    )
        else:
            # Reached a final answer
            return response_message.content
            
    return "Agent stopped: Reached maximum iterations."

if __name__ == "__main__":
    q = "What's due this week?"
    print(f"User: {q}")
    print(f"Agent: {run_agent(q)}")
