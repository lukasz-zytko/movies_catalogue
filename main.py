from random import random
from flask import Flask, render_template, request, redirect, url_for, flash
import tmdb_client
import random
import datetime

app = Flask(__name__)
lists = {
    "popular": "Najpopularniejsze",
    "top_rated": "Najlepiej oceniane",
    "upcoming": "Nadchodzące",
    "now_playing": "Teraz grane"
}
items = [8, 12, 16]
FAVORITES = set()
app.secret_key = b'zosia'

@app.route('/')
def homepage():
    selected_list = request.args.get("list_name", "top_rated")   
    selected_items = request.args.get("how_many",8) 
    if selected_list not in lists:
        movies = tmdb_client.get_movies(how_many=selected_items, list_name="popular")
    else:
        movies = tmdb_client.get_movies(how_many=selected_items, list_name=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, lists=lists, items=items, current_items=selected_items)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie_details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)["cast"]
    movie_images = tmdb_client.get_single_movie_poster_url(movie_id)
    random_image = random.choice(movie_images["backdrops"])
    return render_template("movie_details.html", movie_id=movie_id, movie=movie_details, cast=cast, random_image=random_image)

@app.route("/search")
def search():
    query = request.args.get("q", "avatar")
    search_results = tmdb_client.get_searched_movies(query)["results"]
    results_number = tmdb_client.get_searched_movies(query)["total_results"]
    return render_template("search.html", query=query, search_results=search_results, results_number=results_number)

@app.route("/seriale")
def seriale():
    ile = request.args.get("how_many",8)
    seriale = random.sample(tmdb_client.get_series()["results"],int(ile))
    liczba = tmdb_client.get_series()["total_results"]
    today = datetime.date.today()
    return render_template("seriale.html", seriale=seriale, liczba=liczba, items=items, ile=ile, today=today)

@app.route("/favorites/add", methods=["POST"])
def add_to_favorites():
    data = request.form
    movie_id = data.get("movie_id")
    movie_title = data.get("movie_title")
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f"Film {movie_title} został dodany do ulubionych")
    return redirect(url_for("homepage"))

@app.route("/favorites")
def favorites():
    favorites = []
    for fav in FAVORITES:
        movie = tmdb_client.get_single_movie(fav)
        favorites.append(movie)
    return render_template("favorites.html", movies=favorites)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)

