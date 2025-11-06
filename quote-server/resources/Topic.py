from config import db
from flask import make_response, session, request
from flask_restful import Resource

from models.TopicModel import TopicModel

class TopicList(Resource):
    def get(self):
        topics = [topic.to_dict() for topic in TopicModel.query.all()]
        return topics, 201
    
    def post(self):
        json = request.get_json()
        if json:
            try:
                new_topic = TopicModel(
                    topic = json.get("newTopic"),
                    head_image = json.get("topicImg"),
                    intro = json.get("topicIntro")
                )
                db.session.add(new_topic)
                db.session.commit()
                return new_topic.to_dict(), 201
            
            except ValueError as e:
                return{"error": [str(e)]}, 400