from flask import Flask, request, jsonify
import os
import hoard_db as hdb

app = Flask(__name__)
database_root = os.path.abspath(os.path.dirname(__file__))
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

# update book
@app.route("/book/<id>", methods=["PUT"])
def update_book(id):
    book = hdb.Library.query.get(id)
    title = request.json["title"]
    author = request.json["author"]
    year = request.json["year"]
    month = request.json["month"]
    release_year = request.json["release_year"]
    rating_tag = request.json["rating_tag"]

    book.title = title
    book.author = author
    book.year = year
    book.month = month
    book.release_year = release_year
    book.rating_tag = rating_tag

    db.session.commit()
    return book_schema.jsonify(book)

# delete book
@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    book = hdb.Library.query.get()
    db.session.delete(book)
    db.session.commit()
    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)
