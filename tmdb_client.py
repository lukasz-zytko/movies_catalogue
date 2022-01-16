import requests
import json

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular?language=pl-PL"
    token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyN2VlZjQ4MzYzYmM2MDQ1MjczMjUxYzQ1MzhlMjFjZSIsInN1YiI6IjYxZTAyZTFkNWJjZTllMDA0MTczZTE1ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SZ_UayF2rFJDZtIdnlR2PpauRMVfxU-M8_I6LMYS2Vo"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_poster_url(poster_path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_path}"

def get_movie_info():
    movies_info = {}
    movies = get_popular_movies()['results']
    for movie in movies:
        movies_info[movie['title']] = get_poster_url(movie['poster_path'],'w342')
    return movies_info

def get_movies(how_many):
    data = get_popular_movies()
    return data['results'][:how_many]



