# Imports
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# CONSTANTS
MOVIE_DB_SEARCH_URL = ""
MOVIE_DB_API_KEY = ""
MOVIE_DB_INFO_URL = ""
MOVIE_DB_IMAGE_URL = ""


# Flask Configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)
Bootstrap(app)

# Database Model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# Movie Form
class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

# Update Form
class UpdateForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g. 7.5")
    review = StringField("Your review")
    submit = SubmitField("Submit")


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - 1
    
    db.session.commit()

    return render_template("index.html", movies=movies)

@app.route("/add")
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)

@app.route('/find')
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience 
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

@app.route('/update', methods=["GET", "POST"])
def update():
    form = UpdateForm()

    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
