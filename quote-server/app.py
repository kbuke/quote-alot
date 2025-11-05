from config import api, app 

from resources.Author import AuthorList, Author

from resources.Book import BookList

api.add_resource(AuthorList, "/authors")
api.add_resource(Author, "/authors/<int:id>")

api.add_resource(BookList, "/books")

if __name__ == "__main__":
    app.run(port = 5555, debug = True)