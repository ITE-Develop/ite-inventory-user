from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String, nullable=False)
    image = db.Column(db.String,nullable=False)
    generation = db.Column(db.String, nullable=False)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.String,nullable=False)
    description = db.Column(db.Text)
    expiry_date = db.Column(db.Date)
    purchase_date = db.Column(db.Date)
    location = db.Column(db.String(100))
    users = db.Column(db.String(255))
    category = db.Column(Enum('Furniture', 'Electronic',
                         name='product_category'), nullable=False)
    availability = db.Column(db.String(100))


class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(
        Enum('STEM', 'A', 'B', name='building_rooms'), nullable=False)
    chairs = db.Column(db.Integer, nullable=False)
    num_tables = db.Column(db.Integer, nullable=False)
    board = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String, nullable=False)

