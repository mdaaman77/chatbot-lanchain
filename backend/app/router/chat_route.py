from app.services.chat_service import ChatService
from fastapi import APIRouter
from app.schemas.chat_schemas import ChatRequest

router = APIRouter()




@router.post("/chat")
async def chat(request: ChatRequest):

    response = await ChatService.chat(

        question=request.question,

        history=request.history,

        provider=request.provider,

    )

    return {

        "answer": response

    }