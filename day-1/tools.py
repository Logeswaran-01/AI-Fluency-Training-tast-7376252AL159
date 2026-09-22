import csv
import json
import os

# Paths to data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def read_assignments():
    """Reads the assignments CSV and returns a list of dicts."""
    assignments = []
    try:
        with open(os.path.join(DATA_DIR, 'assignments.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                assignments.append(row)
    except Exception as e:
        return f"Error reading assignments: {e}"
    return json.dumps(assignments)

def read_timetable():
    """Reads the weekly timetable JSON."""
    try:
        with open(os.path.join(DATA_DIR, 'timetable.json'), 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading timetable: {e}"

def read_study_log():
    """Reads the study log markdown file."""
    try:
        with open(os.path.join(DATA_DIR, 'study_log.md'), 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading study log: {e}"

# Tool descriptions for the Agent
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_assignments",
            "description": "Get the current list of assignments, deadlines, estimated hours, and status in JSON format."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_timetable",
            "description": "Get the weekly class timetable in JSON format showing times when you are busy."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_study_log",
            "description": "Get the study log in Markdown format showing topics covered and weak topics."
        }
    }
]

# Mapping function names to actual Python functions
AVAILABLE_FUNCTIONS = {
    "read_assignments": read_assignments,
    "read_timetable": read_timetable,
    "read_study_log": read_study_log,
}
