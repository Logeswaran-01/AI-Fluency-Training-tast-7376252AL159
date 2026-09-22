"""Day 2, Part D: print the agent's real ReAct trace to compare with your paper trace."""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day_1')))

from agent import agent

QUESTION = ("Planning a 5-day Goa trip under Rs. 25,000: is it cheaper to book a "
            "flight with a 3-star hotel for 4 nights, or the same flight with a "
            "4-star hotel for 4 nights that has a 10% early-bird discount? "
            "By how much, and does the cheaper option still leave enough budget "
            "for a Rs. 3,500 scuba diving activity while avoiding rainy days?")

print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")
answer = agent(QUESTION, max_steps=8)
print("\nFINAL ANSWER:", answer)