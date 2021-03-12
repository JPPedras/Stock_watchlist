from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login_page():


    return render_template('login.html')

@auth.route('sign-up',methods=['GET', 'POST'])
def signup_page():

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email too short.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) < 6:
            flash('Password too short.', category='error')
        elif len(username) < 3:
            flash('Username too short.', category='error')
        else:
            flash('Account created succesfully!.', category='success')
        

    return render_template("sign_up.html")

@auth.route('logout')
def logout_page():

    return 'Logout Page'

