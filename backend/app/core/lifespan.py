from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.redis import RedisClient


@asynccontextmanager
async def lifespan(app: FastAPI):

    redis = RedisClient.get_client()

    await redis.ping()

    print("Redis Connected")

    yield

    await redis.close()