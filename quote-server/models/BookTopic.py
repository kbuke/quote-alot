from config import db

from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class BookTopic(db.Model, SerializerMixin):
    __tablename__ = "book_topics"

    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.ForeignKey("books.id"))
    topic_id = db.Column(db.ForeignKey("topics.id"))