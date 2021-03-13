from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login_page():

    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')

        user=User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home_page'))
            else:
                flash('Incorrect password, try again...', category='error')
        else:
            flash('Username does not exist', category='error')
    return render_template('login.html')

@auth.route('sign-up',methods=['GET', 'POST'])
def signup_page():

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user=User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered',category='error')
        if len(email) < 4:
            flash('Email too short.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) < 6:
            flash('Password too short.', category='error')
        elif len(username) < 3:
            flash('Username too short.', category='error')
        else:
            new_user=User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created succesfully!.', category='success')
            return redirect(url_for('views.home_page'))
        

    return render_template("sign_up.html")

@auth.route('logout')
@login_required
def logout_page():
    logout_user()

    return redirect(url_for('auth.login_page'))

