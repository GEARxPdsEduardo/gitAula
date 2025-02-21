
from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from database.settings_db import get_async_db
from modules.auth_module.controller import AuthController
from modules.auth_module.schemas import UserBase, UserResponse
from utils.middleware import Middleware, get_middleware

router = APIRouter()

#  user: parâmetro que recebe os dados do usuário para registro.
#  db: parâmetro que fornece a sessão assíncrona do banco de dados.
#  Depends(get_async_db): injeta automaticamente a sessão do banco de dados na rota.

@router.post('/register')
async def register_user(user: UserBase, db: AsyncSession = Depends(get_async_db)):
    """
    Registra um novo usuário no sistema.
    """
    user_controller = AuthController(db)
    return await user_controller.register_user(user)

@router.post('/login')
async def login_user(user: UserBase, db: AsyncSession = Depends(get_async_db)):
    """
    Autentica um usuário no sistema.
    """
    auth_controller = AuthController(db)
    return await auth_controller.authenticate_user(user)

@router.get('/me', tags=['auth'])
async def me(
    authorization: str = Header(None),
    db: AsyncSession = Depends(get_async_db),
    middleware: Middleware = Depends(get_middleware),
):
    """
    Retorna os detalhes do usuário autenticado.
    """
    user = await middleware.verify_token(authorization)

    return UserResponse(
        id=user.id,
        login=user.a001_login,
        created_at=user.created_at,
        updated_at=user.updated_at
    )    

@router.get('/testando')
async def testando(db: AsyncSession = Depends(get_async_db)):
    """
    Testa rota
    """
    return {"Hello": "World"}