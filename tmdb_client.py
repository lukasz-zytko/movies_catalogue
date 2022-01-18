import requests
import random

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyN2VlZjQ4MzYzYmM2MDQ1MjczMjUxYzQ1MzhlMjFjZSIsInN1YiI6IjYxZTAyZTFkNWJjZTllMDA0MTczZTE1ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SZ_UayF2rFJDZtIdnlR2PpauRMVfxU-M8_I6LMYS2Vo"
language = "?language=pl-PL"

def get_response(url_parameter):
    endpoint = f"https://api.themoviedb.org/3/movie/{url_parameter}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    return response

def get_movies_list(list_name="popular"):
    response = get_response(url_parameter=f"{list_name}{language}")
    return response.json()

def get_single_movie(movie_id):
    response = get_response(url_parameter=f"{movie_id}{language}")
    return response.json()

def get_single_movie_cast(movie_id):
    response = get_response(url_parameter=f"{movie_id}/credits{language}")
    return response.json()["cast"]

def get_single_movie_poster_url(movie_id):
    response = get_response(url_parameter=f"{movie_id}/images")
    return response.json()

def get_poster_url(poster_path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_path}"

def get_movie_info(list_name="popular"):
    movies_info = {}
    movies = get_movies_list(list_name)["results"]
    for movie in movies:
        movies_info[movie["title"]] = {get_poster_url(movie["poster_path"],"w342"): movie["id"]}
    return movies_info

def get_movies(how_many, list_name="popular"):
    data = random.sample(get_movies_list(list_name)["results"],int(how_many))
    return data