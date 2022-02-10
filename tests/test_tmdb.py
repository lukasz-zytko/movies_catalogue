import tmdb_client
from unittest.mock import Mock

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
    # Lista, którą będziemy zwracać przysłonięte "zapytnie do API"
    mock_movies_list = ["Movie 1", "Movie 2"]
    request_mock = Mock()
    # Wynik wywołania zapytania do API
    response = request_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.get_response", request_mock)

    movies_list = tmdb_client.get_movies_list(list_name="popular")
    assert movies_list == mock_movies_list


"""
def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2
"""

