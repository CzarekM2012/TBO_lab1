from project import db, app
import re

# Customer model
#
# Attributes:
# id - Integer
# name - String of length 3-40. May contain letters and whitespaces
# city - String of length 3-30. May contain letters, whitespaces and characters {'-', ',', '.'}
# age - Integer
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        if len(name) < 3 or len(name) > 40:
            raise ValueError('Name of the customer should be between 3 and 40 characters long')
        if re.fullmatch(r'[a-zA-Z\s]{3,40}', name) is None:
            raise ValueError('Name of the customer should contain only letters and spaces')
        self.name = name
        if len(city) < 3 or len(city) > 30:
            raise ValueError('Name of the city should be between 3 and 30 characters long')
        if re.fullmatch(r'[a-zA-Z\s\-,.]{3,30}', city) is None:
            raise ValueError('Name of the city should contain only letters, spaces, hyphens, commas and periods')
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
