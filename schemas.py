# Em schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Esquemas do Pokémon ---
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

# --- Esquemas do Usuário ---
class Usuario(BaseModel):
    id: int
    login: str
    class Config:
        from_attributes = True

# --- Esquemas de Autenticação ---
class TokenData(BaseModel):
    login: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str