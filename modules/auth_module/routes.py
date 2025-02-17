
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.settings_db import get_async_db
from modules.auth_module.controller import AuthController
from modules.auth_module.schemas import UserBase

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


@router.get('/testando')
async def testando(db: AsyncSession = Depends(get_async_db)):
    """
    Testa rota
    """
    return {"Hello": "World"}