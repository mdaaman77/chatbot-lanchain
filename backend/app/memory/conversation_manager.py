import json
from redis.asyncio import Redis

from app.core.redis import RedisClient
from app.config.settings import settings
from pydantic import BaseModel, Field
from typing import List,Literal





class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str




class ConversationManager:
    PREFIX = "chat"

    @classmethod
    def _key(cls,session_id : str) -> str:
        return f"{cls.PREFIX}:{session_id}"


    @classmethod
    async def add_message(cls,session_id:str,message:ChatMessage)-> None:

        redis = RedisClient.get_client()
        key = cls._key(session_id)

        #push messgae in queue
        await redis.lpush(key,  message.model_dump_json())
        await redis.expire(key,settings.SESSION_TTL)


    @classmethod
    async def get_message(cls,session_id:str)-> List[ChatMessage]:
       redis = RedisClient.get_client()
       key = cls._key(session_id=session_id)
       prevMessages =await redis.lrange(key)

       return [
           ChatMessage.model_validate_json(msg)
           for msg in prevMessages
       ]


    @classmethod
    async def delete_chat_session(cls,session_id:str)->None:
        key = cls._key(session_id=session_id)
        redis = RedisClient.get_client()
        present = (redis.exists(key))

        if present is 0: return
        redis.delete(key)
        
         
        


    