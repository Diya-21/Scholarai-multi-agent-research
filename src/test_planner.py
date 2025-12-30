# src/test_planner.py

from agents.planner import PlannerAgent

planner = PlannerAgent()

query = "Explain the role of artificial intelligence in healthcare"
tasks = planner.plan(query)

print("\nGenerated Research Plan:")
for task in tasks:
    print(task)
