from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT

from resources.user import UserRegister
from resources.book import Book, BookList
from resources.library import Library, LibraryList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ekirapa:99405897@localhost/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'amy'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# jwt = (app, authenticate, identity)

api.add_resource(Book, '/book/<string:title>')
api.add_resource(BookList, '/books')
api.add_resource(UserRegister, '/register')
api.add_resource(Library, '/library/<string:name>')
api.add_resource(LibraryList, '/libraries')


if __name__ == '__main__':
    app.run()
