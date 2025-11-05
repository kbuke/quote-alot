from config import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import date

class BookModel(db.Model, SerializerMixin):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    img = db.Column(db.String)
    publication_date = db.Column(db.Date, nullable = True)
    intro = db.Column(db.String)
    pg_count = db.Column(db.Integer)

    # Set up relation with author
    author_id = db.Column(db.ForeignKey("authors.id"))
    author = db.relationship("AuthorModel", back_populates = "books")