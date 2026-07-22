from fastapi import APIRouter, Request, Response

from app.memory.session_manager import SessionManager
from app.schemas.chat_schemas import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()


@router.post("/chat")
async def chat(
    request: Request,
    response: Response,
    payload: ChatRequest,
):

    session_id = SessionManager.get_session_id(
        request=request,
        response=response,
    )

    result = await ChatService.chat(
        session_id=session_id,
        question=payload.question,
        provider=payload.provider,
    )

    return {
        "answer": result
    }