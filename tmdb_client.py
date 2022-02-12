import requests
import random

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyN2VlZjQ4MzYzYmM2MDQ1MjczMjUxYzQ1MzhlMjFjZSIsInN1YiI6IjYxZTAyZTFkNWJjZTllMDA0MTczZTE1ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SZ_UayF2rFJDZtIdnlR2PpauRMVfxU-M8_I6LMYS2Vo"
headers = {"Authorization": f"Bearer {token}"}
language = "?language=pl-PL"

def get_response(url_parameter):
    endpoint = f"https://api.themoviedb.org/3/movie/{url_parameter}"
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
    return response.json()

def get_single_movie_poster_url(movie_id):
    response = get_response(url_parameter=f"{movie_id}/images")
    return response.json()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_movie_info(list_name="popular"):
    movies_info = {}
    movies = get_movies_list(list_name)["results"]
    for movie in movies:
        movies_info[movie["title"]] = {get_poster_url(movie["poster_path"],"w342"): movie["id"]}
    return movies_info

def get_movies(how_many, list_name="popular"):
    data = random.sample(get_movies_list(list_name)["results"],int(how_many))
    return data

def get_searched_movies(search_querry):
    endpoint = f"https://api.themoviedb.org/3/search/movie{language}&query={search_querry}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_series():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today{language}"
    response = requests.get(endpoint,headers=headers)
    return response.json()