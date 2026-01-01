# src/agents/verifier.py

from typing import Dict



class VerifierAgent:
    """
    VerifierAgent evaluates retrieved information
    and filters out weak or misleading content.
    """

    def verify(self, research_data: Dict[str, str]) -> Dict[str, Dict]:
        """
        Takes retrieved research data and returns
        verified, usable information.
        """

        verified_output = {}

        for task, content in research_data.items():

            # Simple rule-based verification (robust + explainable)
            if len(content.strip()) < 40:
                verified_output[task] = {
                    "status": "rejected",
                    "reason": "Content too short or uninformative",
                    "clean_text": ""
                }

            elif "replace doctors" in content.lower():
                verified_output[task] = {
                    "status": "rejected",
                    "reason": "Overgeneralized or misleading claim",
                    "clean_text": ""
                }

            else:
                verified_output[task] = {
                    "status": "verified",
                    "reason": "Relevant and reasonable information",
                    "clean_text": content
                }

        return verified_output
