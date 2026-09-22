# Agentic AI Foundations: Day 1 Task

This repository contains my submission for the Day 1 Task, comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent.

## Folder Structure
- `.venv/`: Python virtual environment (ignored in git).
- `config.py`: Configuration and mock LLM setup.
- `tools.py`: Contains the mock private data and tool functions.
- `chatbot.py`: Plain chatbot implementation.
- `workflow.py`: Rule-based workflow implementation.
- `agent.py`: AI Agent implementation.
- `challenge.py`: Wrapper script to run all three approaches.
- `check_setup.py`: Script to verify environment.
- `analysis.md`: Detailed written analysis of the three approaches.
- `output-screenshots/`: Contains screenshots of the output from `challenge.py`.

## How to Run
1. Ensure you have Python installed.
2. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
3. Install requirements (optional, as scripts are mocked):
   - `pip install -r requirements.txt`
4. Run the challenge script to see all three approaches in action:
   - `python challenge.py`
