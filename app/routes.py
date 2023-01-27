from app import app
from flask import render_template, request, flash, url_for, redirect
from .forms import UserCreationForm
from .models import Product
from flask_login import current_user, login_required


@app.route('/')
@login_required
def homepage():
    posts = Product.query.all()
    print(posts)
    return render_template('home.html', posts = posts)