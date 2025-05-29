from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.schemas import TokenRequest
from app.config import (
    SECRET_KEY,
    ALGORITHM,
)

# Define autenticação com Bearer Token
security = HTTPBearer()

# Criação do router
router = APIRouter()


# Função para criar o token
def create_access_token(username: str = None, expires_delta: int = 30):
    """Cria um token de acesso para o usuario"""
    to_encode = {
        "exp": datetime.utcnow() + (timedelta(minutes=expires_delta)),
        # Uso o generic_user para os casos de teste
        # Mas o usuario seria obrigatorio
        "sub": username if username else "generic_user"
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Função para verificar o token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):  # noqa: E501
    """Verifica se o token utilizado ainda é valido"""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )


# Rota para gerar o token
@router.post("/get-token")
def generate_token(data: TokenRequest):
    access_token = create_access_token(username=data.username)
    return {"access_token": access_token, "token_type": "Bearer"}
