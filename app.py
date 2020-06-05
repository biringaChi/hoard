from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import hoard_db as hdb


# from app import db
# db.create_all()

# Init app
app = Flask(__name__)
mash_mellow = Marshmallow(app)

database_root = os.path.abspath(os.path.dirname(__file__))

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(database_root, "hoard.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

book_schema = hdb.LibrarySchema()
books_schema = hdb.LibrarySchema(many=True)

# create a book
@app.route("/book", methods=["POST"])
def add_book():
    title = request.json["title"]
    author = request.json["author"]
    year = request.json["year"]
    month = request.json["month"]
    release_year = request.json["release_year"]
    rating_tag = request.json["rating_tag"]
    new_book = hdb.Library(title, author, year, month, release_year, rating_tag)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book)

# get a single book
@app.route("/book/<id>", methods=["GET"])
def get_book(id):
    book = hdb.Library.query.get()
    return book_schema.jsonify(book)

# get all books
@app.route("/book", methods=["GET"])
def get_books():
    books = hdb.Library.query.all()
    retrieve = books_schema.dump(books)
    return jsonify(retrieve.data)

if __name__ == '__main__':
    app.run(debug=True)
