from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from models.book import BookModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author',
                        type=str,
                        required=True,
                        help='Every book must have a title.')

    parser.add_argument('library_id',
                        type=int,
                        required=True,
                        help='Every book needs to belong to a library')

    # @jwt_required()
    def get(self, title):
        book = BookModel.find_by_title(title)
        if book:
            return book.json()

        return {'message': 'Book not found.'}, 404

    def post(self, title):
        if BookModel.find_by_title(title):
            return {'message': "A book with name '{}' already exists.".format(title)}, 400

        data = Book.parser.parse_args()
        book = BookModel(title, **data)
        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred inserting the book."}, 500

        return book.json(), 201

    def delete(self, title):
        book = BookModel.find_by_title(title)
        if book:
            book.delete_from_db()

        return {'message': 'item deleted'}

    def put(self, title):
        data = Book.parser.parse_args()
        book = BookModel.find_by_title(title)

        if book is None:
            book = BookModel(title, **data)
        else:
            book.price = data['author']

        book.save_to_db()
        return book.json()


class BookList(Resource):
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}
