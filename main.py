from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = range(1,50)
    number = 8
    return render_template("homepage.html", movies=movies, numer=number)

if __name__ == '__main__':
    app.run(debug=True)

