from uuid import uuid4

SESSION_COOKIE = "chat_session"


class CookieManager:

    @staticmethod
    def generate_session_id() -> str:
        return str(uuid4())