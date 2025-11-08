""" SQLAlchemy query helpers functions"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional
import models

# --- Films---

def get_movie(db:Session, movies_Id: int) -> Optional[models.Movie]:
    """ Retrieve a movie by its ID """
    return db.query(models.Movie).filter(models.Movie.moviesId == movies_Id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """ Retrieve multiple movies with optional filters for title and genre """
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.contains(title))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%genre%"))
        
    return query.offset(skip).limit(limit).all() 

def get_rating(db: Session, user_Id: int, movies_Id: int) -> Optional[models.Rating]:
    """ Retrieve a rating by user ID and movie ID """
    return db.query(models.Rating).filter(
        models.Rating.userId == user_Id,
        models.Rating.moviesId == movies_Id
    ).first()
    
def get_ratings(db: Session, skip: int = 0, limit: int = 100, movies_Id: int = None, user_Id: int = None, min_rating: float = None):
    """ Retrieve multiple ratings """
    query = db.query(models.Rating)
    
    if movies_Id:
        query = query.filter(models.Rating.moviesId == movies_Id)
    if user_Id:
        query = query.filter(models.Rating.userId == user_Id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)
    return query.offset(skip).limit(limit).all()

# ---Tags---

def get_tag(db: Session, user_Id: int, movies_Id: int, tag_text: str) -> Optional[models.Tag]:
    """ Retrieve a tag by user ID, movie ID, and tag text """
    return db.query(models.Tag).filter(
        models.Tag.userId == user_Id,
        models.Tag.moviesId == movies_Id,
        models.Tag.tag == tag_text
    ).first()
    
def get_tags(db: Session, skip: int = 0, limit: int = 100, movies_Id: Optional[int] = None, user_Id: Optional[int] = None):
    """ Retrieve multiple tags """
    query = db.query(models.Tag)
    
    if movies_Id:
        query = query.filter(models.Tag.moviesId == movies_Id)
    if user_Id:
        query = query.filter(models.Tag.userId == user_Id)
        
    return query.offset(skip).limit(limit).all()

# --- Links---

def get_link(db: Session, movies_Id: int) -> Optional[models.Link]:
    """ Retrieve a link by movie ID """
    return db.query(models.Link).filter(models.Link.moviesId == movies_Id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """ Retrieve multiple links """
    return db.query(models.Link).offset(skip).limit(limit).all()

# Analytic Queries 

def get_movie_count(db: Session) -> int:
    """ Retrieve the total number of movies """
    return db.query(models.Movie).count()

def get_rating_count(db: Session) -> int:
    """ Retrieve the total number of ratings """
    return db.query(models.Rating).count()

def get_tag_count(db: Session) -> int:
    """ Retrieve the total number of tags """
    return db.query(models.Tag).count()

def get_link_count(db: Session) -> int:
    """ Retrieve the total number of links """
    return db.query(models.Link).count()