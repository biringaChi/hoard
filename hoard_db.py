from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)

# Init db
db = SQLAlchemy(app)
mash_mellow = Marshmallow(app)

class Library(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    year = db.Column(db.Integer, nullable = True)
    month = db.Column(db.String(10), nullable = True)
    release_year = db.Column(db.Integer, nullable = True)
    rating_tag = db.Column(db.Integer, db.ForeignKey("rating.id"), nullable=True)
    rating = db.relationship("Rating", backref=db.backref("posts", lazy=True))


    def __init__(self, title, author, year, month, release_year):
        self.author = author
        self.title = title
        self.year = year
        self.month = month
        self.release_year = release_year
        self.rating_tag = rating_tag

    def __repr__(self):
        return f"Book name: {self.title}"


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviews = db.Column(db.String(1000), nullable=False)

    def __repr__():
        pass


class LibrarySchema(mash_mellow.Schema):
    """Set fields for display"""
    class Meta:
        fields = ("id", "author", "title", "year", "month", "release_year", "rating_tag")

