from project import db, app
import re


# Book model
#
# Attributes:
# id - Integer
# name - String of length 3-50. May contain letters, whitespaces and characters {'-', ',', ':'}
# author - String of length 3-40. May contain letters and whitespaces
# year_published - Integer
# book_type - String
# status - String
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer)
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        if len(name) < 3 or len(name) > 50:
            raise ValueError('Name of the book should be between 3 and 50 characters long')
        if re.fullmatch(r'[a-zA-Z\s\-,:]{3,50}', name) is None:
            raise ValueError('Name of the book should contain only letters, spaces, hyphens, commas and colons')
        self.name = name
        if len(author) < 3 or len(author) > 40:
            raise ValueError('Name of the author of the book should be between 3 and 40 characters long')
        if re.fullmatch(r'[a-zA-Z\s]{3,40}', author) is None:
            raise ValueError('Name of the author of the book should contain only letters and spaces')
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"


with app.app_context():
    db.create_all()
