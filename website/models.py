from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from yahoo_fin import stock_info as si

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    stocks = db.relationship('Stock')

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(6))
    price = db.Column(db.Float(2))
    change = db.Column(db.Float(2))
    market_cap = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))