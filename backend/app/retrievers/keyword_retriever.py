# app/retrievers/keyword_retriever.py
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi
from app.keyword_search.bm25_store import BM25Store
from app.keyword_search.chunk_store import ChunkStore


class KeywordRetriever:

    def __init__(self):

        self.bm25: BM25Okapi = BM25Store().load()
        self.documents: list[Document] = ChunkStore().load()

        if self.bm25 is None or self.documents is None:
            raise ValueError(
                "BM25 index or ChunkStore not initialized. Run ingestion first!"
            )

    def retrieve(self, query: str, k: int = 10) -> list[Document]:
        tokens = query.lower().split()
        scores = self.bm25.get_scores(tokens)

        
        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True,
        )

        
        top_indices = [
            idx for idx, score in ranked[:k]
            if score > 0
        ]

       
        return [self.documents[i] for i in top_indices]