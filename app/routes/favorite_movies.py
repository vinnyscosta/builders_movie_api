from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.services import OMDBService
from app.routes.auth import verify_token
from app.schemas.favorite_movies import (
    NewMovie,
    FavoriteMoviesResponse,
)
from app.models.favorite_movies import FavoriteMovie
from app.database import get_db

router = APIRouter()


@router.post("/movies", response_model=FavoriteMoviesResponse)
async def create_movie(
    movie: NewMovie,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):
    """Rota para cadastro de filmes favoritos no banco de dados"""

    stmt = select(FavoriteMovie).where(FavoriteMovie.imdb_id == movie.imdb_id)
    result = await db.execute(stmt)
    db_movie = result.scalars().first()

    if db_movie:
        raise HTTPException(
            status_code=400,
            detail="Filme já cadastrado."
        )

    omdb_movie = await OMDBService.get_details(movie.imdb_id)

    if omdb_movie:
        raise HTTPException(
            status_code=400,
            detail="Filme não encontrado para cadastrado."
        )

    # Criando instancia do novo filme
    new_movie = FavoriteMovie(
        imdb_id=omdb_movie.get('imdbID'),
        title=omdb_movie.get('Title'),
        director=omdb_movie.get('Director'),
        writer=omdb_movie.get('Writer'),
        year=omdb_movie.get('Year'),
        poster=omdb_movie.get('Poster', ''),
        plot=omdb_movie.get('Plot', ''),
        country=omdb_movie.get('Country', ''),
        rating=omdb_movie.get('imdbRating'),
    )

    # Criação do filme no banco de dados
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)

    return {"favorite_movies": [new_movie]}


@router.get("/movies/{id}", response_model=FavoriteMoviesResponse)
async def get_movie_by_id(
    id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):
    """Rota para busca de filmes favoritos cadastrados por ID."""
    stmt = select(FavoriteMovie).where(FavoriteMovie.id == id)
    result = await db.execute(stmt)
    db_movie = result.scalars().first()

    if not db_movie:
        raise HTTPException(
            status_code=400,
            detail="Filme não encontrado."
        )

    return {"favorite_movies": [db_movie]}
