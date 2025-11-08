from fastapi import FastAPI,Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal
import query_helpers as helpers
import schemas

# --- Initialize FastAPI app ---
app = FastAPI(
    title="Movies API",
    description="An API to retrieve movie information, ratings, and tags.",
    version="0.1",
) 

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# -- Endpoint to get movie details by ID ---
@app.get("/",
         summary="Get Movie Details by ID",
         description = "Retrieve detailed information about a movie, including ratings, tags, and links, by providing its unique ID.",
         response_description="Detailed information about the movie.",
         operation_id="health_check_movies_api",
         tags = ["monitoring"]
         )

async def root():
    return {"message": "Movies API is up and running!"} 

# -- Endpoint to get an movies using it ID ---

@app.get("/movies/{movies_Id}",summary = "Get movie using its ID", 
         description = "Return the information about movies with respect to thier ID", 
         response_description = "Details about the movies",
         response_model=schemas.MovieDetailed,tags = ["movies"])


def read_movie_by_id( 
     movies_Id: int = Path(..., description="The ID of the movie to retrieve"),
     db: Session = Depends(get_db),):
     db_movie = helpers.get_movie(db, movies_Id)
     if db_movie is None:
         raise HTTPException(status_code=404, detail="Movie not found")
     return db_movie



# -- Endpoint to get a list of movies with pagination and optional filters title, genre, skip, limit --

@app.get(
    "/movies",
    summary= "List the movies",
    description = "Return a list of movies with pagination and optionals filters, either by title or genres",
    response_description = "A list of movies",
    response_model = List[schemas.MovieSimple],
    tags = ["movies"],
) 

def movies_list(
    skip: int = Query(0, ge = 0, description = "Number of results that should be skipped"),
    limit: int = Query(100, le = 1000, description= "Maximum number of returned results"),
    title: str = Query(None, description = "Filter movies by title"),
    genre: str = Query(None, description= "Filter movies by genre"),
    db: Session = Depends(get_db)
):
    movies = helpers.get_movies(db, skip = skip, limit = limit, title = title, genre = genre)
    return movies

# -- Endpoint to get an evaluation with respect to the user and movie --

@app.get(
    "/ratings/{user_Id}/{movies_Id}",
    summary= "Get an evaluation over user and movie",
    description = "Return evaluation of an user for a given movie",
    response_description  = "Evaluation details",
    response_model = schemas.RatingSimple,
    tags = ["Evaluation"]
)

def read_rating(
    user_Id: int = Path(..., description = "User ID"),
    movies_Id: int = Path(..., description = "Movie ID"),
    db: Session = Depends (get_db)
):
    rating = helpers.get_rating(db, user_Id = user_Id, movies_Id= movies_Id)
    if rating is None:
        raise HTTPException (
            status_code = 404,
            detail = f"Any evaluation found for user {user_Id} and for the movie {movies_Id}"
    )
    return rating


# -- Endpoint to get a list of evaluation with filters --

@app.get(
    "/ratings",
    summary = "List of evaluations",
    description = "Return a list of evaluations with pagination and optional filters (movie, user, note min)",
    response_description = "List of evaluations",
    response_model = List[schemas.RatingSimple],
    tags = ["Evaluations"]
)

def list_ratings(
    skip: int = Query(0, ge = 0, description = "Number of results that should be skipped"),
    limit: int = Query(100, le= 1000, description = "Maximun number of return results"),
    movies_Id: Optional[int] = Query(None, description = "Filters using movies ID"),
    user_Id: Optional[int] = Query(None, description = "Filter using user ID"),
    min_rating: Optional[float] = Query(None, ge=0.0, le = 5.0, description = "Filter rating greater or equal to this values"),
    db: Session = Depends(get_db) 
):
    ratings = helpers.get_ratings(db, skip = skip, limit = limit, movies_Id= movies_Id, user_Id= user_Id, min_rating = min_rating)
    return ratings

# -- Endpoint to return tag with respect to user and given movie --

@app.get(
    "/tags/{user_Id}/{movies_Id}/{tag_text}",
    summary= "Get a specific tag",
    description= "Return a tag by user and given movie",
    response_description = "Simple tag",
    response_model = schemas.TagSimple,
    tags = ["tags"],
)

def read_tag(
    user_Id:int = Path(..., description = "User ID"),
    movies_Id: int = Path (..., description = "Movie ID"),
    tag_text: str = Path(..., description = "Exact contente of tag"),
    db: Session = Depends(get_db)
):
    result = helpers.get_tag(db, user_Id=user_Id, movies_Id=movies_Id, tag_text = tag_text)
    if result is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Tag not found for user {user_Id}, the movie {movies_Id} and the tag '{tag_text}'"
        )
    return result


# -- Endpoint to return a list of tags with pagination and optional filters by user or movie --

@app.get(
    "/tags",
    summary = "List of tags",
    description = "Return a list of tags with pagination and optional filters by user or movie",
    response_description = "Get list of tags",
    response_model= List[schemas.TagSimple],
    tags = ["tags"]
)

def list_tags(
    skip: int = Query(0, ge = 0, description = "Numbers of results that should be skipped"),
    limit: int = Query(100, le= 1000, description = "Maximun number of returned results"),
    movies_Id: Optional[int]= Query(None, description = "Filter by movie ID"),
    user_Id: Optional[int] =  Query(None, description = "Filter by user ID"),
    db: Session = Depends(get_db)
):
    return helpers.get_tags(db, skip = skip, limit = limit, movies_Id = movies_Id, user_Id = user_Id)


# -- Endpoint to return the IMDB and TMDB ID for given movie --

@app.get(
    "/links/{movies_Id}",
    summary = "Get the link of the movie",
    description = "Return the IMDB and TMDB ID for given movie.",
    response_description = "Get link",
    response_model = schemas.LinkSimple,
    tags = ["link"]
)

def read_link(
    movies_Id: int = Path(..., description = "Movie ID"),
    db: Session = Depends(get_db)
):
    result = helpers.get_link(db, movies_Id = movies_Id)
    if result is None:
        raise HTTPException (status_code = 404,
                             detail = f"Any movie link don't found with the ID{movies_Id}")
    return result


# -- Endpoint to return a paginated list of IMDB and TMDB ID of all teh movies --

@app.get(
    "/links",
    summary = "List of the movies links",
    description = "Return a list of paginated IMDB and TMDB ID for all movies.",
    response_description = "Get all list of movies links",
    response_model = List[schemas.LinkSimple],
    tags = ["links"]
)

def list_links(
    skip: int =Query(0, ge = 0, description = "Number of results that should be skipped"),
    limit: int = Query(100, le= 1000, description = "Maximun number of returned results"),
    db: Session = Depends(get_db)
):
    return helpers.get_links(db, skip = skip, limit = limit)


# -- Endpoint to statistics on the database --

@app.get(
    '/analytics',
    summary = "Get the statistics",
    description= """
    Return a analytic  summary of database:
    - Total number of movies
    - Total number of evaluations
    - Total number of tags
    - Total number of links towars IMDB/TMDB
    """,
    response_description = "All database statistcs",
    response_model= schemas.AnalyticsResponse,
    tags = ["analytics"]
)

def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)

    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count
    )
