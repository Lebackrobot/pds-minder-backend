import hashlib

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.api.deps import get_db
from src.crud.crud_usuario import crud_usuario
from src.models.usuario_model import UsuarioModel
from src.schemas.schema_usuario import UsuarioCreateSchema

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(response: Response, payload: UsuarioCreateSchema, db: Session = Depends(get_db)):
    usuario = crud_usuario.get_by_username(db=db, username=payload.username)

    if usuario:
        response.status_code = status.HTTP_409_CONFLICT
        return {'success': False, 'message': 'usuario já existe'}


    return crud_usuario.create_user(db=db, usuario=UsuarioModel(
        nome=payload.nome,
        username=payload.username,
        password=hashlib.sha256(payload.password.encode('utf-8')).hexdigest(),
        email=payload.email
    ))
