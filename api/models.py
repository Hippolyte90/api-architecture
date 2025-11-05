"""SQLAlchemy models"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship # to ensure relationships between tables
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    moviesid = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String)
    
    ratings = relationship("Rating", back_populates ="movie", cascade = "all, delete")
    tags = relationship("Tag", back_populates="movie", cascade="all, delete")
    links = relationship("Link", back_populates="movie", uselist = False, cascade="all, delete")
    
    
class Rating(Base):
    __tablename__ = "ratings"

    userId = Column(Integer, primary_key=True)
    moviesId = Column(Integer, ForeignKey("movies.moviesid"), primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="ratings")
    
class Tag(Base):
    __tablename__ = "tags"

    userId = Column(Integer, primary_key=True)
    moviesId = Column(Integer, ForeignKey("movies.moviesid"), primary_key=True)
    tag = Column(String, primary_key=True)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="tags")
    
class Link(Base):
    __tablename__ = "links"

    moviesId = Column(Integer, ForeignKey("movies.moviesid"), primary_key=True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)

    movie = relationship("Movie", back_populates="links")