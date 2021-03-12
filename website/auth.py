from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():

    return 'Login Page'

@auth.route('sign-up')
def signup_page():

    return 'Sign-up Page'

@auth.route('logout')
def logout_page():

    return 'Logout Page'

