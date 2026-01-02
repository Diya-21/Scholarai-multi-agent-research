ScholarAI is a verification-first Generative AI research assistant designed to reduce hallucinations and explicitly communicate answer reliability.
Unlike traditional chatbots, ScholarAI separates planning, retrieval, verification, and synthesis into independent agents and dynamically switches between evidence-based and analytical answer modes.Key Features

 Multi-Agent Architecture
Planner, Retriever, Verifier, and Writer agents operate independently.

 Smart Information Retrieval
Uses query expansion, Wikipedia filtering, and relevance scoring to avoid low-quality sources.

Verification & Confidence Scoring
Each response is verified and tagged with confidence levels (High / Medium / Low).

 Hallucination-Aware Answer Modes
Automatically switches between:

Evidence-Based Mode (when strong sources exist)

Analytical Mode (expert synthesis when sources are weak)

 Streamlit Web Interface
Clean UI displaying raw evidence, verification status, confidence, and final answer.

 Secure API Handling
Uses environment variables for Gemini API keys (no secrets in code).

System Architecture
User Query
    ↓
Planner Agent        → breaks question into research tasks
    ↓
Retriever Agent      → fetches relevant information + relevance score
    ↓
Verifier Agent       → evaluates reliability & confidence
    ↓
Writer Agent         → synthesizes final answer
    ↓
Streamlit UI         → displays answer mode & confidence

 Why This Project Matters

Most AI tools always produce confident answers, even when evidence is weak.
ScholarAI instead prioritizes honesty, transparency, and safety, making it suitable for:

Education

Research assistance

AI content validation

Enterprise AI guardrails

 Tech Stack

Python 3.13

Streamlit (UI & deployment)

Gemini API (google-genai)

Wikipedia API







Just tell me 👍
