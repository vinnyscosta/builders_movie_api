from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class OMDBType(str, Enum):
    """Enum para as opções de busca"""
    all_types = "all_types"
    movie = "movie"
    series = "series"
    episode = "episode"


class SearchItem(BaseModel):
    Title: str
    Year: str
    imdbID: str
    Type: OMDBType
    Poster: Optional[HttpUrl]


class SearchResponse(BaseModel):
    Search: List[SearchItem]
    totalResults: str
    Response: str


class DetailResponse(BaseModel):
    Title: str
    Year: str
    Rated: Optional[str]
    Released: Optional[str]
    Runtime: Optional[str]
    Genre: Optional[str]
    Director: Optional[str]
    Writer: Optional[str]
    Actors: Optional[str]
    Plot: Optional[str]
    Language: Optional[str]
    Country: Optional[str]
    Awards: Optional[str]
    Poster: Optional[HttpUrl]
    imdbRating: Optional[str]
    imdbVotes: Optional[str]
    imdbID: str
    Type: OMDBType
    Response: str
