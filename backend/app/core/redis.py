from redis.asyncio import Redis

from app.config.settings import settings


class RedisClient:
    _redis: Redis | None = None

    @classmethod
    def get_client(cls) -> Redis:

        if cls._redis is None:

            cls._redis = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD,
                decode_responses=True,
            )

        return cls._redis