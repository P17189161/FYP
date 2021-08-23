from flask import render_template, request, flash
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/seminars')
@login_required
def seminars():
    return render_template("seminars.html", user=current_user)