from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ValidationError

class UserBase(BaseModel):
    login: str = Field(..., example="john_doe")
    codigo: str = Field(..., example="123")
    senha: str = Field(
        ...,
        min_length=8,
        description="A senha deve ter no mínimo 8 caracteres, conter pelo menos uma letra maiúscula, um número e um caractere especial.",
        example="Password@123"
    )

    @field_validator("codigo")
    @classmethod
    def validar_codigo(cls, value: str) -> str:
        if value != "khhum":
            raise ValueError("Código Inválido.")
        return value

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, value: str) -> str:
        if not any(char.isupper() for char in value):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        if not any(char.isdigit() for char in value):
            raise ValueError("A senha deve conter pelo menos um número.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in value):
            raise ValueError("A senha deve conter pelo menos um caractere especial.")
        return value
    funcao: str = Field(..., example="teste")

    class Config:
        json_schema_extra = {
            "example": {
                "login": "john_doe",
                "codigo": "khhum",
                "senha": "Password@123",
                "funcao": "teste"
            }
        }

class UserResponse(BaseModel):
    id: int = Field(..., example=1)
    login: str = Field(..., example="john_doe")
    created_at: datetime = Field(..., example="2023-10-24T12:34:56")
    updated_at: Optional[datetime] = Field(None, example="2023-10-24T12:35:56") 
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "login": "john_doe",
                "created_at": "2023-10-24T12:34:56",
                "updated_at": "2023-10-24T12:35:56"
            }
        }
