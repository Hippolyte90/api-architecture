# MovieLens API

Welcome into API **MovieLens** - an API RESTful developped with **FastAPI** to explore MovieLens database. This API allow you to query a lot of informations on the movies like, his evaluations, his users, his tags and also the links towars external databases (IMDB,TMDB).

## Main Features

- Research the movies using title, genre, or ID
- Consulting evaluations by user and movie
- Manage the tags related to movies
- Retrieve IMDB ID
- Global basics statistics 

---

## Requirements

- Python >= 3.12
- An support HTTP as `httpx` or `requests`
  
Quickly installation of `httpx`:

```bash
pip install httpx

```
---

## Stat using API

This API is accessible at the following web adresse:

```
hhtp://localhost:8000
```

The Swaqqer UI is available here:

```
http://localhost:8000/docs
```

---

## Relevent endpoints

|Method | URL                                       | Description                          |
|-------|-------------------------------------------|--------------------------------------|
|Get    | `/`                                       | Check the API healthy                |
|Get    | `/movies`                                 | Paged list of the movies with filters|
|Get    | `/movies/{movies_Id}`                     | Detail of a movie                    |
|Get    | `/ratings`                                | Paged list of evaluations            |
|Get    | `/ratings/{user_Id}/{movies_Id}`          | Movie evaluation given by an user    |
|Get    | `/tags`                                   | List of tags                         |
|Get    | `tags/{user_Id}/{movies_Id}/{tag}`        | Tag's detail                         |
|Get    | `links`                                   | List of IMDB/TMDB ID                 |
|Get    | `links/{movies_Id}`                       | Identifiers for a given movie        |
|Get    | `/analytics`                              | Basics statistics                    |

---

## Usage examples with `httpx`

### List of movies

```python
import httpx
response = httpx.get("http://localhost:8000/movies", params = {"limit":5})
print(response.json())
```

### Get specific movie

```python
movies_Id = 1
response = httpx.get("http://localhost:8000/movies/{movies_Id}")
print(response.json)
```

### Research the evaluations of given movie

```python
response = httpx.get("http://localhost:8000/ratings", params = {"movies_Id": 1})
print(response.json)
```

### Retrieve specific tag

```python
response = httpx.get("http://localhost:8000/tags/5/1/superbe")
print(response.json())
```

### Get global statistics

```python
response = httpx.get("http://localhost:8000/analytics")
print(response.json())
```
---

## Usage conditions

- This API is designed for educational and experimental purposes.
- Please do not make bulk calls without frequency control (rate-limiting is not implemented yet).
- You can use in your notebooks, apps or dataviz projects to visualize teh MovieLens data.

---

## Contribution

Your contributions are welcome !

- Improve the request performances
- Add new endpoints
- Make the API available on public host

---

## Useful resources

- Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
- Technical documentation : available via Swagger
- MovieLens database : [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)


