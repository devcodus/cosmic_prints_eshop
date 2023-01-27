from app import app
from flask import render_template, flash, url_for, redirect
from .models import Product
from flask_login import current_user, login_required


@app.route('/')
@login_required
def homepage():
    posts = Product.query.all()
    print(posts)
    return render_template('home.html', posts = posts)
    
@app.route('/cart')
@login_required
def cart():
    
    message = 'This item has been added to your cart!'

    # addedtocart = current_user
    # print(addedtocart)

    return render_template('cart.html', message = message)

