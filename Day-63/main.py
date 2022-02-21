# Imports
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Flask Configurations
app = Flask(__name__)

# Database Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app=app)


# TABLE MODEL
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

db.create_all()


@app.route('/')
def home():
    books = Book.query.all()

    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        form = request.form

        name = form.get("name")
        author = form.get("author")
        rating = form.get("rating")
        
        new_book = Book(title=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form.get("id")
    
        book = Book.query.get(book_id)

        new_rating = request.form.get("rating")
        book.rating = new_rating
        
        db.session.commit()

        return redirect(url_for("home"))
    
    book_id = request.args.get('id')
    book = Book.query.get(book_id)

    return render_template("edit.html", book=book)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    book = Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

