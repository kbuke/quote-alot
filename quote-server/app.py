from config import api, app 

from resources.Author import AuthorList

from resources.book import BookList

api.add_resource(AuthorList, "/authors")

api.add_resource(BookList, "/books")

if __name__ == "__main__":
    app.run(port = 5555, debug = True)