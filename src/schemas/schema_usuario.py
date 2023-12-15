from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsuarioBaseSchema(BaseModel):
    username: str
    nome: str
    password: str
    email: str


class UsuarioCreateSchema(UsuarioBaseSchema):
    ...


class UsuarioDBSchema(UsuarioBaseSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
