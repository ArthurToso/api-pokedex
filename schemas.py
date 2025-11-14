from pydantic import BaseModel, Field
from typing import List, Optional

class PokemonBase(BaseModel):
    nome: str
    tipo: str
    habilidades: List[str] = Field(..., min_length=1, max_length=3)

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int
    dono_login: str
    class Config:
        from_attributes = True 

class Usuario(BaseModel):
    id: int
    login: str
    class Config:
        from_attributes = True

class TokenData(BaseModel):
    login: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str