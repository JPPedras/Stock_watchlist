from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    stocks = db.relationship('Stock')

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(6), unique=True)
    change = db.Column(db.Float(2))
    price = db.Column(db.Float(2))
    price_target = db.Column(db.Float(2))
    buy_rating = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))