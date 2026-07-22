# app/keyword_search/chunk_store.py
import pickle
from pathlib import Path
from langchain_core.documents import Document

class ChunkStore:
    CHUNK_PATH = Path("app/keyword_search/chunks.pkl")

    @classmethod
    def save(cls, documents: list[Document]):
        cls.CHUNK_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(cls.CHUNK_PATH, "wb") as f:
            pickle.dump(documents, f)

    @classmethod
    def load(cls) -> list[Document] | None:
        if not cls.CHUNK_PATH.exists():
            return None
        with open(cls.CHUNK_PATH, "rb") as f:
            return pickle.load(f)