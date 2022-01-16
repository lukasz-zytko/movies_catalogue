from random import random
from flask import Flask, render_template
import tmdb_client
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(8)
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie_details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_single_movie_poster_url(movie_id)
    random_image = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie_id=movie_id, movie=movie_details, cast=cast, random_image=random_image)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)

