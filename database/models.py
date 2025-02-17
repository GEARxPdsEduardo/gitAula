from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .settings_db import Base  

class a001Usuario(Base):
    __tablename__ = 'a001_usuarios'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
    a001_login = Column(String(50), nullable=False, unique=True)
    a001_senha = Column(String(256), nullable=False)
    a001_codigo = Column(String(10), nullable=False)
    a001_funcao = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())  

class a002Licenca(Base):
    __tablename__ = 'a002_licenca'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
    a002_cnpj = Column(String(30), nullable=False, unique=True)  
    a002_cliente = Column(String(50), nullable=True)
    a002_ativo = Column(String(3), nullable=True)
    a002_renomear = Column(String(3), nullable=True)
    a002_aviso = Column(String(100), nullable=True)
    a002_data_hora = Column(String(30), nullable=True)
    a002_sql = Column(Text, nullable=True)
    a002_validade_licenca = Column(DateTime, nullable=True)
    a002_product_key = Column(String(50), nullable=True)
    a002_product_key_token = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, onupdate=func.now())