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

    stmt = select(FavoriteMovie).where(
        FavoriteMovie.imdb_id == movie.imdb_id,
        FavoriteMovie.user == user
    )
    result = await db.execute(stmt)
    db_movie = result.scalars().first()

    if db_movie:
        raise HTTPException(
            status_code=400,
            detail="Filme já cadastrado."
        )

    omdb_movie = await OMDBService.get_details(movie.imdb_id)

    if not omdb_movie:
        raise HTTPException(
            status_code=400,
            detail="Filme não encontrado para cadastrado."
        )

    # Criando instancia do novo filme
    new_movie = FavoriteMovie(
        imdb_id=omdb_movie.get('imdbID'),
        user=user,
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
    stmt = select(FavoriteMovie).where(
        FavoriteMovie.id == id,
        FavoriteMovie.user == user
    )
    result = await db.execute(stmt)
    db_movie = result.scalars().first()

    if not db_movie:
        raise HTTPException(
            status_code=404,
            detail="Filme não encontrado."
        )

    return {"favorite_movies": [db_movie]}


@router.get("/movies", response_model=FavoriteMoviesResponse)
async def get_all_movies(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):
    """Rota para busca de todos os filmes favoritos cadastrados."""
    stmt = select(FavoriteMovie).where(
        FavoriteMovie.user == user
    )
    result = await db.execute(stmt)
    db_movie = result.scalars().all()

    if not db_movie:
        raise HTTPException(
            status_code=404,
            detail="Nenhum Filme cadastrado."
        )

    for movie in db_movie:
        movie.imdb_id = movie.imdb_id or ""
        movie.title = movie.title or ""
        movie.director = movie.director or ""
        movie.writer = movie.writer or ""
        movie.year = movie.year or ""
        movie.rating = movie.rating or ""

    return {"favorite_movies": db_movie}
