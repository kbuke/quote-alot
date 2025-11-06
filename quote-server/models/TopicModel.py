from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class TopicModel(db.Model, SerializerMixin):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key = True)
    topic = db.Column(db.String, nullable = False, unique = True)
    head_image = db.Column(db.String, nullable = False)
    intro = db.Column(db.String)

    # Set up many-to-many relation with books
    books = db.relationship("BookModel", back_populates = "topics", secondary = "book_topics")

    serialize_rules = (
        "-books.topics",
        "-books.author",
    )