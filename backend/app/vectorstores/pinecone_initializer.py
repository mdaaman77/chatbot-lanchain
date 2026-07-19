from pinecone import Pinecone, ServerlessSpec

from app.config.settings import settings


class PineconeInitializer:

    @staticmethod
    def initialize():

        pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

        existing_indexes = [
            index.name
            for index in pc.list_indexes()
        ]

        if settings.PINECONE_INDEX_NAME in existing_indexes:
            return

        pc.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1",
            ),
        )