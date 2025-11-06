from config import api, app 

from resources.Author import AuthorList, Author

from resources.Book import BookList

from resources.Topic import TopicList

from resources.BookTopic import BookTopicList

api.add_resource(AuthorList, "/authors")
api.add_resource(Author, "/authors/<int:id>")

api.add_resource(BookList, "/books")

api.add_resource(TopicList, "/topics")

api.add_resource(BookTopicList, "/booktopics")

if __name__ == "__main__":
    app.run(port = 5555, debug = True)