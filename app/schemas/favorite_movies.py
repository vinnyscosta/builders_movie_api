from pydantic import BaseModel
from typing import List


class FavoriteMovie(BaseModel):
    id: int
    imdb_id: str
    title: str
    director: str
    writer: str
    year: str
    poster: str
    plot: str
    country: str
    rating: str

    class Config:
        orm_mode = True


class FavoriteMoviesResponse(BaseModel):
    favorite_movies: List[FavoriteMovie]


class NewMovie(BaseModel):
    imdb_id: str
