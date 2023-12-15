from sqlalchemy import Column, DateTime, Integer, MetaData, String, func

from src.database.db_connect import Base


class UsuarioModel(Base):
    __tablename__ = 'usuario'
    metadata = MetaData(schema='usuario')

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: str = Column(String(100), nullable=False)
    username: str = Column(String(100), nullable=False)
    password: str = Column(String(100), nullable=False)
    email: str = Column(String(100), nullable=False)  
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

