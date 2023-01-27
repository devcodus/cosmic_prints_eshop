from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


addproduct = db.Table(
    'addproduct',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('item_name', db.String, db.ForeignKey('product.item'), nullable=False)
)



class  User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    cart = db.relationship("Product",
        secondary = addproduct,
        backref=db.backref('addtocart', lazy='dynamic'),
        lazy='dynamic'

    )
    

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def saveToCart(self, save):
        db.cart.add(save) # what does save mean?
        db.session.commit()

    def removeFromCart(self, user):
        db.cart.delete(user)
        db.session.commit()

class  Product(db.Model):
    __tablename__= 'product'
    item_id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50), nullable=False, unique=True)
    img_url = db.Column(db.String(1000), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, unique=True)

    


    def __init__(self, item,img_url,price):
        self.item = item
        self.img_url = img_url
        self.price = price
  

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()