from config import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import date, datetime

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

    serialize_rules = (
        "-books.author",
    )

    @validates("birth_date", "death_date")
    def validate_dates(self, key, value):
        # 1 - Check if dates have been inputted
        if value and not isinstance(value, date):
            try:
                value = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Must enter a valid date")
        
        # 2 - Check that birth_date is before death_date
        birth_date = value if key == "birth_date" else self.birth_date
        death_date = value if key == "death_date" else self.death_date 

        if birth_date and death_date:
            if death_date <= birth_date:
                raise ValueError("Death date must be after birth date")
        
        return value