# src/agents/writer.py

from typing import Dict


class WriterAgent:
    """
    WriterAgent converts verified research
    into a clean, readable final answer.
    """

    def write(self, verified_data: Dict[str, Dict]) -> str:
        sections = []

        for task, result in verified_data.items():
            if result["status"] == "verified":
                section = f"### {task}\n{result['clean_text']}"
                sections.append(section)

        if not sections:
            return "Insufficient verified information to generate an answer."

        final_answer = (
            "## AI in Healthcare – Research Summary\n\n"
            + "\n\n".join(sections)
        )

        return final_answer
