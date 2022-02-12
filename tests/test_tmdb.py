import tmdb_client
from unittest.mock import Mock
from main import app
import pytest

@pytest.mark.parametrize("category, status", (
  ("popular", 200),
  ("top_rated", 200)
))

def test_homepage(monkeypatch, category, status):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.get_movies", api_mock)

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == status
        api_mock.assert_called_once_with(how_many=8,list_name=category)


"""
def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_path = "some_poster_path"
    expected_default_size = "w342"
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_path=poster_path)
    # Porównanie wyników
    #assert expected_default_size in poster_url
    assert poster_url == "https://image.tmdb.org/t/p/w342/some_poster_path"

def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_name="popular")
    assert movies_list is not None

def test_get_movies_list(monkeypatch):
    mock_movies_list = ["Movie 1", "Movie 2"]
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.get_response", request_mock)

    movies_list = tmdb_client.get_movies_list(list_name="popular")
    assert movies_list == mock_movies_list

def test_single_movie_cast(monkeypatch):
    mock_movie_cast = ["Actor 1", "Actor 2"]
    request_mock = Mock()
    response = request_mock.return_value
    response.json.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.get_response", request_mock)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id=1)
    assert movie_cast == mock_movie_cast

def test_get_response_endpoint(monkeypatch):
    mock_endpoint = "https://api.themoviedb.org/3/movie/test"
    endpoint_mock = Mock()
    endpoint_mock.return_value = "https://api.themoviedb.org/3/movie/test"
    monkeypatch.setattr("tmdb_client.requests.get", endpoint_mock)
    test_endpoint = tmdb_client.get_response(url_parameter="test")
    assert test_endpoint == mock_endpoint

def test_get_movies(monkeypatch):
    how_many = 2
    test_movies = ["Movie 1", "Movie 2"]
    mock_list = Mock()
    mock_list.return_value = test_movies
    monkeypatch.setattr("tmdb_client.random.sample",mock_list)
    movies = tmdb_client.get_movies(how_many=how_many, list_name="popular")
    assert test_movies == movies
"""


