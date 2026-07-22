from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Google
    GOOGLE_API_KEY: str
    GEMINI_MODEL: str = "gemini-3.1-flash-lite"

    # Pinecone
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str

    # Hugging Face
    HUGGINGFACE_API_KEY: str
    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    # Ollama
    OLLAMA_MODEL: str = "phi3"

    # Default Provider
    MODEL_PROVIDER: str = "gemini"

    #redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int = 0
    REDIS_PASSWORD: str | None = None
 
    SESSION_TTL: int = 1800

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()