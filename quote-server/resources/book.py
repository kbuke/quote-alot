from flask import make_response, session, request
from flask_restful import Resource

from models.BookModel import BookModel

from config import db 

class BookList(Resource):
    def get(self):
        books = [book.to_dict() for book in BookModel.query.all()]
        return books, 201 
    
    def post(self):
        json = request.get_json()
        breakpoint()
        if json:
            try:
                new_book = BookModel(
                    name = json.get("bookName"),
                    img = json.get("bookImg"),
                    publication_date = json.get("publishDate"),
                    intro = json.get("bookIntro"),
                    pg_count = json.get("pgNumber"),
                    author_id = json.get("authorId")
                )
                db.session.add(new_book)
                db.session.commit()
                return new_book.to_dict(), 201 
            
            except ValueError as e:
                return{"error": [str(e)]}, 400