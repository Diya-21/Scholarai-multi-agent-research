from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.verifier import VerifierAgent
from agents.writer import WriterAgent

planner = PlannerAgent()
retriever = RetrieverAgent()
verifier = VerifierAgent()
writer = WriterAgent()

query = "Explain the role of artificial intelligence in healthcare"

tasks = planner.plan(query)
retrieved_data = retriever.retrieve(tasks)
verified_data = verifier.verify(retrieved_data)
final_answer = writer.write(verified_data)

print("\n📝 FINAL GENERATED ANSWER:\n")
print(final_answer)
