from sqlalchemy import Column, Integer, String
from app.database import Base


class FavoriteMovie(Base):
    __tablename__ = "favorite_movies"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    imdb_id = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    writer = Column(String)
    year = Column(String)
    poster = Column(String, nullable=True)
    plot = Column(String, nullable=True)
    country = Column(String, nullable=True)
    rating = Column(String)
