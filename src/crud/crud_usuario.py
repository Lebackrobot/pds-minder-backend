import hashlib

from sqlalchemy.orm import Session

from src.models.usuario_model import UsuarioModel


class CRUDUsaurio:
    @staticmethod
    def get_by_username(db: Session, username: str) -> UsuarioModel:
        return db.query(UsuarioModel).where(UsuarioModel.username == username).first()
    

    @staticmethod
    def create_user(db: Session, usuario: UsuarioModel) -> UsuarioModel:
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        return usuario

crud_usuario = CRUDUsaurio()