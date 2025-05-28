from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas import (
    OMDBType,
    SearchResponse,
    DetailResponse,
)
from app.services import OMDBService

router = APIRouter()


# Rota para buscar produções
@router.get("/search/{prod_type}", response_model=SearchResponse)
async def search_by_title(
    prod_type: OMDBType,
    title: str = Query(),
    year: Optional[int] = Query(None, alias="y"),
    page: Optional[int] = Query(1)
):
    """Busca produções com filtros baseados na API do OMDb"""
    response = await OMDBService.search(
        title=title,
        prod_type=prod_type.value,
        year=year,
        page=page
    )

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Erro Durante a busca no OMDb."
        )

    return response


# Rota para buscar detalhes de uma produção
@router.get("/details/{id}", response_model=DetailResponse)
async def get_production_details(id: str) -> dict:
    """Busca detalhes de um filme na api do OMDb"""
    response = await OMDBService.get_details(id)

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Erro Durante a busca no OMDb."
        )

    return response
