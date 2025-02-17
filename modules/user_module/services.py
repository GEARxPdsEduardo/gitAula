
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import a001Usuario

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db  # Sessão assíncrona do banco de dados


    async def get_user_by_login(self, user_login: str) -> Optional[a001Usuario]:
        """
        Busca um usuário no banco de dados pelo login.

        Parâmetros:
        - user_login (str): O login do usuário a ser buscado.

        Retorno:
        - Retorna um objeto do tipo a001Usuario se encontrado, ou None caso contrário.
        """
        result = await self.db.execute(select(a001Usuario).filter(a001Usuario.a001_login == user_login))
        return result.scalar()
    
    async def create_user(self, login: str, hashed_password: str, codigo: str, funcao: str) -> Optional[a001Usuario]:
        db_user = a001Usuario(
            a001_login=login,
            a001_senha=hashed_password,
            a001_codigo=codigo,
            a001_funcao = funcao
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user