from typing import Literal

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

from app.config.settings import settings

load_dotenv()


class LLMFactory:


    @staticmethod
    def getLlm(
        provider : Literal["gemini","ollama"] | None = None
    ):
        provider = provider or settings.MODEL_PROVIDER

        temperature = 0

        if provider=="gemini":
            return ChatGoogleGenerativeAI(
                model=settings.GEMINI_MODEL,
                temperature=temperature
            )


        else:
            return ChatOllama(
                model=settings.OLLAMA_MODEL,
                temperature=temperature
            )

        raise ValueError(f"Unsupported provider: {provider}")