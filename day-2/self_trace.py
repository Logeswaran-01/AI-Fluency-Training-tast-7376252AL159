"""Day 2, Part B: the same question asked WITHOUT and WITH Chain-of-Thought."""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day_1')))

from config import client, MODEL, banner

QUESTIONS = [
    # 1. Multi-step arithmetic
    "A trip to Goa costs Rs. 9,200 for flights, Rs. 7,600 for a 4-night hotel stay, "
    "and Rs. 3,500 for a scuba diving activity. A 5% booking convenience fee is added "
    "to the total, and the traveler pays the final amount in 3 equal instalments. "
    "How much is each instalment?",
    # 2. Counting in two parts
    "An adventure park in Goa offers 6 rides. In the morning each ride runs 4 batches, "
    "and in the afternoon each ride runs 5 batches. How many total batches run across "
    "all rides in one day?",
    # 3. Ordering / logic
    "Resort A is more expensive than Resort B. Resort B is more expensive than Resort C. "
    "Resort D is cheaper than Resort C. Which resort is the most expensive and which is "
    "the cheapest?",
]

DIRECT_PROMPT = "You are a helpful assistant. Give only the final answer. Do not explain."

COT_PROMPT = ("You are a helpful assistant. Solve the problem step by step. "
              "Number each step and show the calculation in that step. "
              "After the steps, write the last line exactly as: Final Answer: <answer>")

def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": question}],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    banner("CHAIN-OF-THOUGHT COMPARISON — GOA TRIP PLANNING")
    for number, question in enumerate(QUESTIONS, start=1):
        print("=" * 72)
        print(f"QUESTION {number}: {question}\n")
        print("--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question), "\n")
        print("--- WITH CoT ---")
        print(ask(COT_PROMPT, question), "\n")