from typing import AsyncGenerator
from fastapi import Header, Depends
from database.models import a001Usuario
from database.settings_db import get_async_db
from .token import Token
from .http_responses import error
from modules.user_module.services import UserService
from sqlalchemy.ext.asyncio import AsyncSession
import os

class Middleware:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.token_handler = Token()
        self.user_service = UserService(db)
        

    async def verify_token(self, authorization: str) -> a001Usuario:
        if not authorization:
            raise error("Invalid token", 401)

        login = self.token_handler.get_login_from_token(authorization)
        user = await self.user_service.get_user_by_login(login)
        if not user:
            raise error("Invalid token", 401)
        return user
        
# Factory function for FastAPI dependency injection
def get_middleware(db: AsyncSession = Depends(get_async_db)) -> Middleware:
    return Middleware(db)