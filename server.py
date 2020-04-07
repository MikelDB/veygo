from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from models import Cart, Element, Discount

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/test'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'This is going to be my home page'


@app.route('/cart', methods=['POST'])
def create_cart():
    return 'Cart created'


@app.route('/cart/<cart_id>', methods=['GET'])
def get_cart(cart_id):
    return 'You cart %s' % escape(cart_id)


@app.route('/cart/<cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    return 'You cart %s has been deleted' % escape(cart_id)


@app.route('/cart/<cart_id>', methods=['POST'])
def add_item(cart_id):
    return 'Element added to cart %s' % escape(cart_id)


@app.route('/cart/<cart_id>/<item_id>', methods=['DELETE'])
def delete_item(cart_id, item_id):
    return 'Element deleted'


@app.route('/cart/<cart_id>/discount/<discount_code>', methods=['POST'])
def add_discount(cart_id, discount_code):
    return 'Discount code applied'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
