# %%
from hmoviessdk import MovieClient, MovieConfig


# Initilisation of the client with the API URL
config = MovieConfig(movie_base_url="https://api-architecture.onrender.com")
client = MovieClient(config=config)

# 1. Health check
print("Health check:")
print(client.health_check())


# %%
# 2. Retrieve movie using it ID
print("\n Movie ID 1:")
movie = client.get_movie(1)
print(movie)
print(type(movie))


# %%
# 3. List of movies (first 5)
print("\n List of movies:")
movies = client.list_movies(limit=5)
print(type(movies))
for m in movies:
    print(m)
    print(type(m))

# %%
# 4. Retrieve specific rating
print("\n Rating for user 1 and movie 1:")
rating = client.get_rating(user_Id=1, movies_Id=1)
print(rating)
print(type(rating))


# %%
# 5. Movies 's link
print("\n Link for movie ID 1:")
link = client.get_link(movies_Id=1)
print(link)
print(type(link))


# %%
# 6. Analytics
print("\n Analytics:")
analytics = client.get_analytics()
print(analytics)
print(type(analytics))


# %%
# 7. Test with option to choose the output format
# By default: Pydantic Object
new_movies = client.list_movies(limit=5)
print(new_movies)
print(type(new_movies))


# %%
    # Dictionnary format 
new_movies_dicts = client.list_movies(limit=5, output_format="dict")
print(new_movies_dicts)
print(type(new_movies_dicts))

 #%%
    # DataFrame format 
new_movies_df = client.list_movies(limit=5, output_format="pandas")
print(new_movies_df)
print(type(new_movies_df))
# %%
