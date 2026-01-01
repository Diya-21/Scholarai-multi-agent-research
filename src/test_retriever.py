from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent

planner = PlannerAgent()
retriever = RetrieverAgent()

query = "Explain the role of artificial intelligence in healthcare"

tasks = planner.plan(query)
research_notes = retriever.retrieve(tasks)

print("\nRetrieved Research Notes:\n")
for task, content in research_notes.items():
    print(f"\n🔹 {task}")
    print(content)
