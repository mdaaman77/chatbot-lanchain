from fastapi import Request, Response

from app.core.cookies import (
    CookieManager,
    SESSION_COOKIE,
)


class SessionManager:

    @staticmethod
    def get_session_id(
        request: Request,
        response: Response,
    ) -> str:

        session = request.cookies.get(
            SESSION_COOKIE
        )

        if session:

            return session

        session = CookieManager.generate_session_id()

        response.set_cookie(

            key=SESSION_COOKIE,

            value=session,

            httponly=True,

            samesite="lax",

            max_age=1800,
        )

        return session