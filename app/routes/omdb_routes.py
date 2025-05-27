from fastapi import APIRouter, HTTPException
from app.services import OMDBService

router = APIRouter()


# Rota para buscar filmes
@router.get("/search/{movie_name}", response_model=dict)
async def search_movie_by_name(movie_name: str) -> dict:
    """Busca Filmes baseado na api do OMDb"""
    response = await OMDBService.search_movie(movie_name)

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Erro Durante a busca no OMDb."
        )

    return response


# Rota para buscar detalhes de filmes
@router.get("/details/{movie_id}", response_model=dict)
async def get_movie_details(movie_id: str) -> dict:
    """Busca detalhes de um filme na api do OMDb"""
    response = await OMDBService.get_movie_details(movie_id)

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Erro Durante a busca no OMDb."
        )

    return response
