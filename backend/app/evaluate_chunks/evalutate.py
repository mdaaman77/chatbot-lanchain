# app/evaluate_chunks/evaluate.py
from typing import List
from langchain_core.documents import Document


class EvaluateChunks:

    def __init__(self, threshold: float = 0.5):
        """
        :param threshold: Minimum relevance/rerank score required to pass.
        """
        self.threshold = threshold

    def pass_threshold(self, docs: List[Document]) -> List[Document]:
        """
        Filters documents based on whether their rerank score meets the threshold.
        """
        filtered_docs = []

        for doc in docs:
            # Rerankers typically store scores under 'score' or 'relevance_score' in metadata
            score = doc.metadata.get("score") or doc.metadata.get("relevance_score", 0.0)

            if score >= self.threshold:
                filtered_docs.append(doc)

        print(f"--- THRESHOLD EVALUATION ---")
        print(f"Retrieved: {len(docs)} docs | Passed threshold ({self.threshold}): {len(filtered_docs)} docs")

        return filtered_docs