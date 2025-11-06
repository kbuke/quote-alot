from config import api, app 

from resources.Author import AuthorList, Author

from resources.Book import BookList

from resources.Topic import TopicList

api.add_resource(AuthorList, "/authors")
api.add_resource(Author, "/authors/<int:id>")

api.add_resource(BookList, "/books")

api.add_resource(TopicList, "/topics")

if __name__ == "__main__":
    app.run(port = 5555, debug = True)