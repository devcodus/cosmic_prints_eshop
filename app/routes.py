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
    

@app.route('/<item_name>', methods = ['GET', 'POST'])
@login_required
def addToCart(item_name):
    addedItem = Product.query.filter_by(item = item_name).first()
    print(addedItem)
    
    current_user.saveToCart(addedItem)
    

    return redirect(url_for('cart'))

@app.route('/cart')
@login_required
def cart():
    
    message = 'This item has been added to your cart!'

    # addedtocart = current_user
    # print(addedtocart)

    return render_template('cart.html', message = message)

