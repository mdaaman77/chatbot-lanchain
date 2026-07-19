from langchain_huggingface import HuggingFaceEndpointEmbeddings

from app.config.settings import settings
from dotenv import load_dotenv

load_dotenv()



class EmbeddingsFactory:

    @staticmethod
    def get_embeddings():
        return HuggingFaceEndpointEmbeddings(
            model= settings.EMBEDDING_MODEL,
            huggingfacehub_api_token=settings.HUGGINGFACE_API_KEY
        )


    

