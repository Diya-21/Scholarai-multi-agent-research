from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.verifier import VerifierAgent

planner = PlannerAgent()
retriever = RetrieverAgent()
verifier = VerifierAgent()

query = "Explain the role of artificial intelligence in healthcare"

tasks = planner.plan(query)
retrieved_data = retriever.retrieve(tasks)
verified_data = verifier.verify(retrieved_data)

print("\n✅ Verified Research Output:\n")

for task, result in verified_data.items():
    print(f"\n▶ {task}")
    print("Status:", result["status"])
    print("Reason:", result["reason"])
    print("Content:", result["clean_text"])
