import hashlib

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.api.deps import get_db, autenticar_usuario

router = APIRouter()


@router.post('/', status_code=status.HTTP_200_OK)
def signin(response: Response, usuario = Depends(autenticar_usuario), db: Session = Depends(get_db)):
    
    if not usuario:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return { 'success': False, 'message': 'usuario ou senha incorreta' }
    
    return usuario 


