from app import app
from flask import render_template, flash, url_for, redirect, request
import requests
from .models import Product
from flask_login import current_user, login_required


@app.route('/')
@login_required
def populate():

    url = "https://api.nasa.gov/planetary/apod?api_key=kFHR3AFVVyE6UWjaIGXtd1dHO4ey1Z9SZcGlG6J0&start_date=2022-12-01&end_date=2023-01-01"

    monthly_apod = {}

    response = requests.get(url)
    if response.status_code == 200:
        apod_month_list = response.json()
        # print(apod_month_list)
        for apod in apod_month_list:
            monthly_apod['item_name'] = apod['title']
            monthly_apod['img_url'] = apod['url']
            monthly_apod['price'] = 20 # RNG here next

            item_name = monthly_apod['item_name']
            img_url = monthly_apod['img_url']
            price =  monthly_apod['price']

            product = Product(item_name, img_url, price)
            product.saveToDB()

            # posts = Product.query.all()

            continue
            # return render_template('home.html', posts = posts)

    posts = Product.query.all()
    print(posts)
    return render_template('home.html', posts = posts)

@app.route('/all_products')
def displayProducts():
    
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
    deletedcart = Product.query.filter_by(item_name=item_name).first()
    # deletedcart = current_user.cart
    print(deletedcart)
    if deletedcart:
        current_user.deleteFromCart(deletedcart)

    return redirect(url_for('cart'))
    # return render_template('cart.html')


