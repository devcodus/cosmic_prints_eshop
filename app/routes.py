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
    addedItem = Product.query.filter_by(item_name = item_name).first()
    print(addedItem)
    # if addedItem:
    current_user.saveToCart(addedItem)


    return redirect(url_for('cart'))

@app.route('/cart', methods = ['GET', 'POST'])
@login_required
def cart():
    
    usercart= current_user.cart
    message = 'This item has been added to your cart!'
    
    
    

    return render_template('cart.html', usercart=usercart, message = message)

@app.route('/cart/<string:item_name>', methods=['GET', 'POST'])
@login_required
def removeFromCart(item_name):
    print(item_name)
    deletedcart = Product.query.filter_by(item=item_name).first()
    # deletedcart = current_user.cart
    print(deletedcart)
    if deletedcart:
        current_user.deleteFromCart(deletedcart)

    return redirect(url_for('cart'))
    # return render_template('cart.html')
