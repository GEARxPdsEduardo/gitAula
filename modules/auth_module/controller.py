
import bcrypt
from modules.auth_module.schemas import UserBase
from modules.user_module.services import UserService
from sqlalchemy.ext.asyncio import AsyncSession

from utils.http_responses import error, log_only, success  # Importando a função de log
from utils.token import Token  # Importando a função de log

class AuthController:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_service = UserService(db)
        self.token_handler = Token()

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
        
         # Criando user no bd
        new_user = await self.user_service.create_user(user.login, hashed_password_str, user.codigo, user.funcao)

        # Retorna se a operação foi concluída com sucesso ou não.
        if new_user:
            return success("Conta criada com sucesso!", None, 201)
        else:
            return error("Um erro ocorreu, tente novamente mais tarde", 500)
        
    async def authenticate_user(self, user:UserBase):
        existing_user = await self.user_service.get_user_by_login(user.login)

        if not user or not bcrypt.checkpw(user.senha.encode('utf-8'), existing_user.a001_senha.encode('utf-8')):
            return error('Login ou senha incorretos', 422)
        
        access_token = self.token_handler.generate_token(existing_user)
        if access_token:
            return success('Login realizado com sucesso!', {"token": access_token}, 200)
        else:
            return error("Um erro ocorreu, tente novamente mais tarde", 500)
