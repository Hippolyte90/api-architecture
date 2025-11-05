""" SQLAlchemy query helpers functions"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional
import models

# --- Films---

def get_movie(db:Session, movie_id: int) -> Optional[models.Movie]:
    """ Retrieve a movie by its ID """
    return db.query(models.Movie).filter(models.Movie.moviesid == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """ Retrieve multiple movies with optional filters for title and genre """
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.contains(title))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%genre%"))
        
    return query.offset(skip).limit(limit).all() 

def get_rating(db: Session, user_id: int, movie_id: int) -> Optional[models.Rating]:
    """ Retrieve a rating by user ID and movie ID """
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.moviesId == movie_id
    ).first()
    
def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None, min_rating: float = None):
    """ Retrieve multiple ratings """
    query = db.query(models.Rating)
    
    if movie_id:
        query = query.filter(models.Rating.moviesId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)
    return query.offset(skip).limit(limit).all()

# ---Tags---

def get_tag(db: Session, user_id: int, movie_id: int, tag_text: str) -> Optional[models.Tag]:
    """ Retrieve a tag by user ID, movie ID, and tag text """
    return db.query(models.Tag).filter(
        models.Tag.userId == user_id,
        models.Tag.moviesId == movie_id,
        models.Tag.tag == tag_text
    ).first()
    
def get_tags(db: Session, skip: int = 0, limit: int = 100, movie_id: Optional[int] = None, user_id: Optional[int] = None):
    """ Retrieve multiple tags """
    query = db.query(models.Tag)
    
    if movie_id:
        query = query.filter(models.Tag.moviesId == movie_id)
    if user_id:
        query = query.filter(models.Tag.userId == user_id)
        
    return query.offset(skip).limit(limit).all()

# --- Links---

def get_link(db: Session, movie_id: int) -> Optional[models.Link]:
    """ Retrieve a link by movie ID """
    return db.query(models.Link).filter(models.Link.moviesId == movie_id).first()

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