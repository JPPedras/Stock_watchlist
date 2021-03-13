from flask import Blueprint, render_template, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from yahoo_fin import stock_info as si
from yahoofinancials import YahooFinancials as yf
from . import db
from .models import Stock
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home_page():

    if request.method=='POST':
        ticker=request.form.get('ticker').upper()

        if yf(ticker).get_current_price() != None:
            new_stock=Stock(ticker=ticker, price=yf(ticker).get_current_price(), change=yf(ticker).get_current_percent_change(), market_cap=yf(ticker).get_market_cap(), user_id=current_user.id)
            db.session.add(new_stock)
            db.session.commit()
        else:
            flash('Invalid Ticker',category='error')

    return render_template('home.html', user=current_user)

@views.route('/delete-stock', methods=['POST'])
def delete_stock():
    stock = json.loads(request.data)
    stockId = stock['stockId']
    stock = Stock.query.get(stockId)
    if stock:
        if stock.user_id == current_user.id:
            db.session.delete(stock)
            db.session.commit()

    return jsonify({})
        
