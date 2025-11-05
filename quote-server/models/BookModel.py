from config import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import date, datetime
from models.AuthorModel import AuthorModel

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

    serialize_rules = (
        "-author.books",
    )

    @validates("author_id", "publication_date")
    def validate_author_info(self, key, value):
        # 1 - Ensure author is registered
        if key == "author_id":
            existing_author = AuthorModel.query.filter(AuthorModel.id == value).first()
            if not existing_author:
                return {"error": f"Author {id} is not registered on the application."}
        
        # 2 - Ensure publication date is of date format
        if key == "publication_date":
            try:
                value = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Publication date must be a valid date")
        
        # 3 - Check that book is not published before authors birth date
        author_id = value if key == "author_id" else self.author_id
        publication_date = value if key == "publication_date" else self.publication_date

        if author_id:
            existing_author = AuthorModel.query.filter(AuthorModel.id == author_id).first()
            if existing_author and publication_date <= existing_author.birth_date:
                raise ValueError("The publication date must be after the authors birth")
        
        return value
        