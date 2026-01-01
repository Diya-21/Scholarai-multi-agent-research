import streamlit as st

from src.agents.planner import PlannerAgent
from src.agents.retriever import RetrieverAgent
from src.agents.verifier import VerifierAgent
from src.agents.writer import WriterAgent

# Page config
st.set_page_config(page_title="ScholarAI – Research Assistant", layout="wide")

st.title("📚 ScholarAI – Multi-Agent Research Assistant")
st.write(
    "This system plans, retrieves, verifies, and writes research answers using a multi-agent GenAI pipeline."
)

# Input box
query = st.text_area(
    "Enter your research question:",
    placeholder="e.g. Explain the role of artificial intelligence in healthcare"
)

if st.button("Run Research"):
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        with st.spinner("Planning research..."):
            planner = PlannerAgent()
            tasks = planner.plan(query)

        st.subheader("🧠 Research Plan")
        for t in tasks:
            st.markdown(f"- {t}")

        with st.spinner("Retrieving information..."):
            retriever = RetrieverAgent()
            retrieved_data = retriever.retrieve(tasks)

        with st.spinner("Verifying information..."):
            verifier = VerifierAgent()
            verified_data = verifier.verify(retrieved_data)

        st.subheader("✅ Verified Information")
        for task, result in verified_data.items():
            st.markdown(f"**{task}**")
            st.write(f"Status: {result['status']}")
            if result["status"] == "verified":
                st.write(result["clean_text"])
            st.markdown("---")

        with st.spinner("Writing final answer..."):
            writer = WriterAgent()
            final_answer = writer.write(verified_data)

        st.subheader("📝 Final Answer")
        st.markdown(final_answer)
