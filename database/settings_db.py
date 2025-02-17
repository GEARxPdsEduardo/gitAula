from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Define a URL de conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

# Cria o motor de banco de dados assíncrono
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

# Define a classe base para os modelos
Base = declarative_base()

# Dependência para sessão de banco de dados
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()