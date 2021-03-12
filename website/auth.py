from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():

    return render_template('login.html')

@auth.route('sign-up')
def signup_page():

    return render_template("sign_up.html")

@auth.route('logout')
def logout_page():

    return 'Logout Page'

