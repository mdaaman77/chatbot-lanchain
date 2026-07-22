# app/keyword_search/bm25_store.py
import pickle
from pathlib import Path
from rank_bm25 import BM25Okapi

class BM25Store:
    INDEX_PATH = Path("app/keyword_search/bm25.pkl")

    @classmethod
    def save(cls, bm25: BM25Okapi):
        cls.INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(cls.INDEX_PATH, "wb") as f:
            pickle.dump(bm25, f)

    @classmethod
    def load(cls) -> BM25Okapi | None:
        if not cls.INDEX_PATH.exists():
            return None
        with open(cls.INDEX_PATH, "rb") as f:
            return pickle.load(f)