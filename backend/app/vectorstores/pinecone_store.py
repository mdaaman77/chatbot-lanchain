from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from app.config.settings import settings
from app.embeddings.factory import EmbeddingsFactory


class PineconeStore:

    @staticmethod
    def get_vector_store():

        # Connect to Pinecone
        Pinecone(api_key=settings.PINECONE_API_KEY)

        embeddings = EmbeddingsFactory.get_embeddings()

        return PineconeVectorStore(
            index_name=settings.PINECONE_INDEX_NAME,
            embedding=embeddings,
        )