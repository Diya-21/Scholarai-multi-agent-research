
# src/agents/planner.py

import os
import time
from typing import List
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()


class PlannerAgent:
    """
    PlannerAgent breaks a complex research query
    into smaller, logical sub-questions.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        # Initialize Gemini client
        self.client = genai.Client(api_key=api_key)

        # Free-tier friendly, stable model
        self.model_name = "models/gemini-flash-latest"

    def plan(self, query: str) -> List[str]:
        """
        Takes a research query and returns
        a list of structured sub-tasks.
        """

        prompt = f"""
You are a research planner.

Break the following research question into
4 to 6 clear, logical sub-questions.

Research Question:
{query}

Return ONLY a numbered list.
"""

        # Small delay to avoid rate-limit bursts
        time.sleep(1)

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        raw_text = response.text

        tasks = []
        for line in raw_text.split("\n"):
            line = line.strip()
            if line and line[0].isdigit():
                tasks.append(line)

        return tasks
