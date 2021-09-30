from db import db


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))

    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))
    library = db.relationship('LibraryModel')

    def __init__(self, title, author, library_id):
        self.title = title
        self.author = author
        self.library_id = library_id

    def json(self):
        return {'title': self.title, 'author': self.author}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
