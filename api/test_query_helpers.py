from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# Test get_movie

movies  =  get_movies(db, limit = 10)

for movie in movies:
    print(f"Movie ID: {movie.moviesid}, Title: {movie.title}, Genres: {movie.genres}")

db.close()