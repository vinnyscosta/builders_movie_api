from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services import OMDBService
from app.routes import (
    auth_router,
    desafio_router,
    omdb_router,
)
from app.config import TOKEN_OMDB

# Configuração da classe de integração do OMDB
OMDBService.configure(api_key=TOKEN_OMDB)

# Criação da instancia do FastAPI
app = FastAPI(
    title="Desafio Builders",
    description="API para criação de listas de filmes personalizadas.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Incluir rotas
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(
    desafio_router,
    prefix="/desafio",
    tags=["Desafio Builders"],
)

app.include_router(
    omdb_router,
    prefix="/omdb",
    tags=["OMDb"],
)
