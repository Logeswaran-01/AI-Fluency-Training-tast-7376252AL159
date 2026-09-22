import json
from config import get_llm_response
from tools import read_assignments, read_timetable, read_study_log

def run_workflow(question: str) -> str:
    """
    Rule-based workflow: Fixed pipeline.
    1. Loads data explicitly based on strict logic.
    2. Formats a prompt template.
    3. Uses LLM *only* to format the output.
    """
    # 1. Load data
    assignments = json.loads(read_assignments())
    timetable = read_timetable()
    study_log = read_study_log()
    
    # 2. Rule-based sorting (e.g. sorting assignments by estimated hours descending)
    # Note: Sorting by string 'deadline' is tricky in rules without datetime parsing, 
    # but we can sort by hours easily to show rule logic.
    sorted_assignments = sorted(assignments, key=lambda x: int(x['estimated_hours']), reverse=True)
    
    # 3. Prompt Template
    prompt = f"""
Given the following data:
Assignments (sorted by most hours):
{json.dumps(sorted_assignments, indent=2)}

Timetable:
{timetable}

Study Log:
{study_log}

User Question: {question}

Please answer the user's question purely based on the provided data above. Do not hallucinate.
    """
    
    # 4. LLM call
    system_msg = "You are a formatter that answers questions using ONLY the provided context."
    response = get_llm_response(prompt, system_message=system_msg)
    return response

if __name__ == "__main__":
    q = "What's due this week?"
    print(f"User: {q}")
    print(f"Workflow: {run_workflow(q)}")
