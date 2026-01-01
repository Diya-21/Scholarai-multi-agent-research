# src/agents/retriever.py

import wikipedia
from typing import Dict, List


class RetrieverAgent:
    """
    RetrieverAgent fetches relevant information
    for each research sub-task.
    """

    def __init__(self):
        wikipedia.set_lang("en")

    def retrieve(self, tasks: List[str]) -> Dict[str, str]:
        """
        Takes a list of research tasks and returns
        raw information for each task.
        """

        research_data = {}

        for task in tasks:
            try:
                summary = wikipedia.summary(task, sentences=3)
                research_data[task] = summary
            except wikipedia.exceptions.DisambiguationError as e:
                research_data[task] = f"Ambiguous topic. Possible meanings: {e.options[:5]}"
            except wikipedia.exceptions.PageError:
                research_data[task] = "No relevant Wikipedia page found."
            except Exception as e:
                research_data[task] = f"Error retrieving data: {str(e)}"

        return research_data
