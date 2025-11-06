from config import db

from flask import make_response, session, request
from flask_restful import Resource

from models.BookTopic import BookTopic

class BookTopicList(Resource):
    def get(self):
        book_topics = [book_topic.to_dict() for book_topic in BookTopic.query.all()]
        return book_topics, 200
    
    def post(self):
        json = request.get_json()

        if json:
            try:
                new_book_topic = BookTopic(
                    book_id = json.get("bookId"),
                    topic_id = json.get("topicId")
                )
                db.session.add(new_book_topic)
                db.session.commit()
                return new_book_topic.to_dict(), 201 
            except ValueError as e:
                return {"error": [str(e)]}, 400

    
