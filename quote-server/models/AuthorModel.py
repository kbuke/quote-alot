from config import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import date

class AuthorModel(db.Model, SerializerMixin):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    img = db.Column(db.String)
    nationality = db.Column(db.String)
    birth_date = db.Column(db.Date)
    death_date = db.Column(db.Date)
    intro = db.Column(db.String)

    # SET UP RELATION WITH BOOKS THEY HAVE WROTE
    books = db.relationship("BookModel", back_populates = "author", cascade = "all, delete-orphan")