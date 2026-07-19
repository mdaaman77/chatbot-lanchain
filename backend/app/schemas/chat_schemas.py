from pydantic import BaseModel,Field
from typing import List,Literal


class ChatRequest(BaseModel):
    question:str = Field(required= True,description="question asked by user"),
    history:List[str] = Field(description="chat history with user"),
    provider: Literal["gemini","ollama"]

    class Config:
        from_attributes = True