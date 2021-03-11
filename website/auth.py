from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():

    return 'Login Page'


@auth.route('/register')
def register_page():

    return 'Register Page'

