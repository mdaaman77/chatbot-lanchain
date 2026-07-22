from rank_bm25 import BM25Okapi
from langchain_core.documents import Document


from app.keyword_search.bm25_store import BM25Store
from app.keyword_search.chunk_store import ChunkStore

class BM25Index:

    @staticmethod
    def build(documents: list[Document]) -> BM25Okapi:

        tokenized_corpus = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        bm25 = BM25Okapi(tokenized_corpus)
        BM25Store.save(bm25)
        ChunkStore.save(documents)

        return bm25