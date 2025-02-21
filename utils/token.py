import os
from dotenv import load_dotenv
import pytz
import jwt
from datetime import datetime, timedelta
from database.models import a001Usuario
from .http_responses import error
import random

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Token:
    def __init__(self):
        self.secret = os.getenv("JWT_KEY")
        if not self.secret:
            raise ValueError("JWT_KEY environment variable is not set.")
        self.tz = pytz.timezone("America/Sao_Paulo")

    def generate_token(self, user: a001Usuario) -> str:
        payload = {
            'iat': datetime.now(tz=self.tz),  # Data de emissão
            'exp': datetime.now(tz=self.tz) + timedelta(days=5),  # Expiração em 5 dias
            'login': user.a001_login  # Identificador do usuário
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def get_login_from_token(self, authorization: str) -> str:
        if not authorization or not isinstance(authorization, str):
            raise error('Authorization header is missing or invalid', 401)
        
        token_parts = authorization.split()
        
        if len(token_parts) != 2 or token_parts[0] != 'Bearer':
            raise error('Invalid token format', 401)
        
        encoded_token = token_parts[1]
        try:
            decoded_token = jwt.decode(encoded_token, self.secret, algorithms=['HS256'])
            login = decoded_token.get('login')
            
            if not login:
                raise error('Invalid token', 401)
            return login
        except jwt.ExpiredSignatureError:
            raise error('Token expired', 401)
        except jwt.DecodeError:
            raise error('Invalid token', 401)