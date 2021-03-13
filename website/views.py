from flask import Blueprint, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home_page():
    return render_template('home.html')
