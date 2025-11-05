from models.AuthorModel import AuthorModel

from flask import make_response, session, request
from flask_restful import Resource

from config import db

class AuthorList(Resource):
    def get(self):
        authors = [author.to_dict() for author in AuthorModel.query.all()]
        return authors, 201 
    
    def post(self):
        json = request.get_json()
        breakpoint()
        if json:
            try:
                new_author = AuthorModel(
                    name = json.get("authorName"),
                    img = json.get("authorImg"),
                    nationality = json.get("nationality"),
                    birth_date = json.get("birthday"),
                    death_date = json.get("deathday"),
                    intro = json.get("authorIntro")
                )
                db.session.add(new_author)
                db.session.commit()
                return new_author.to_dict(), 201 
            
            except ValueError as e:
                return{"error": [str(e)]}, 400

class Author(Resource):
    def get(self, id):
        author = AuthorModel.query.filter(AuthorModel.id == id).first()
        if author:
            return author.to_dict(), 201 
        else:
            return{"error": f"Author {id} not found"}
    
    def delete(self, id):
        author = AuthorModel.query.filter(AuthorModel.id == id).first()
        if author:
            db.session.delete(author)
            db.session.commit()
            return{"message": f"Author {id} deleted"}, 201 
        else:
            return{"error": f"Author {id} not found"}, 404
            
            