from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

movies = db.query(Movie).limit(10).all()

# movies

# for movie in movies:
#    print(f"Movie ID: {movie.moviesid}, Title: {movie.title}, Genres: {movie.genres}")
   
# Query the movies that the genre is Action

# action_movies= db.query(Movie).filter(Movie.genres.contains("Action")).limit(20).all()

# for action in action_movies:
#    print(f"Movie ID: {action.moviesid}, \nTitle: {action.title},\n Genres: {action.genres}")   
   
# Recover some ratings

# ratings = db.query(Rating).filter(Rating.moviesId == 1).all()

# for rate in ratings:
#    print(f"User ID: {rate.userId}, Movie ID: {rate.moviesId}, Rating: {rate.rating}, Timestamp: {rate.timestamp}")

# Retrieve the movies that have a rating greater than 4

high_ratings_movies = db.query(Movie.title ,Rating.rating).filter(Rating.rating >4).limit(20).all()

for high_rate_title, rat in high_ratings_movies:
     print(f"User title: {high_rate_title}, Rating: {rat}")
   
   
# Close the session
db.close()