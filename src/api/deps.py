import hashlib

from fastapi import Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from src.core.settings import settings
from src.crud.crud_usuario import crud_usuario

DB_CONNECTION = settings.DB_CONNECTION

engine = create_engine(DB_CONNECTION, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def autenticar_usuario(credentials: HTTPBasicCredentials, db: Session = Depends(get_db)):
    usuario = crud_usuario.get_by_username(db=db, username=credentials.username)
    password_payload = hashlib.sha256(credentials.password.encode('utf-8')).hexdigest()

    if not usuario or password_payload != usuario.password:
        return
    
    return usuario