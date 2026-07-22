# app/retrievers/hybrid_retriever.py
from langchain_core.documents import Document
from app.retrievers.retriever import RetrieverFactory
from app.retrievers.keyword_retriever import KeywordRetriever


class HybridRetriever:

    def __init__(self):
        self.vector = RetrieverFactory.get_retriever(k=10)
        # KeywordRetriever automatically loads chunks.pkl & bm25.pkl!
        self.keyword = KeywordRetriever()

    async def retrieve(
        self,
        query: str,
    ) -> list[Document]:

        vector_docs = await self.vector.ainvoke(query)
        keyword_docs = self.keyword.retrieve(query, k=10)

        merged = []
        seen = set()

        for doc in vector_docs + keyword_docs:
            text = doc.page_content

            if text not in seen:
                seen.add(text)
                merged.append(doc)

        return merged[:20]