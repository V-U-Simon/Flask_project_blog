from pprint import pprint
from marshmallow import Schema, fields


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Nested(lambda: AuthorSchema(exclude=("books",)))


class AuthorSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    books = fields.List(fields.Nested(BookSchema(exclude=("author",))))


user = User("Vasia", email="alsdfjk@sldfk.ru")
book_1 = Book("Article_1", user)
book_2 = Book("Article_2", user)



book_schema = BookSchema()
res = book_schema.dump(book_1)
pprint(res, indent=2)


# author_result = AuthorSchema().dump(user)
# pprint(author_result, )

# print(res, type(res))
