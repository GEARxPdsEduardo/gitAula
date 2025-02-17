import bcrypt
from modules.auth_module.schemas import UserBase
from modules.user_module.services import UserService
from sqlalchemy.ext.asyncio import AsyncSession

from utils.http_responses import error, log_only, success  # Importando a função de log

class AuthController:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_service = UserService(db)

    async def register_user(self, user: UserBase):
        # log_only("Acessou corretamente")
        return success("Cadastrado com sucesso!", None, 201)
        print(user)
        
    async def register_user(self, user: UserBase):
        print(user)
        # Verifica se o login informado já está cadastrado no sistema.
        existing_user = await self.user_service.get_user_by_login(user.login)

        if existing_user:
            return error("Este login já está em uso.", 422)

        # Criptografa a senha utilizando a biblioteca bcrypt.
        senha = "Password@123"
        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())


        # Convertendo bytes para string
        hashed_password_str = hashed_senha.decode('utf-8')
       
        new_user = await self.user_service.create_user(user.login, hashed_password_str, user.codigo, user.funcao)

        # Retorna se a operação foi concluída com sucesso ou não.
        if new_user:
            return success("Conta criada com sucesso!", None, 201)
        else:
            return error("Um erro ocorreu, tente novamente mais tarde", 500)