from app import app, models, db
from markupsafe import escape

@app.route('/')
def home():
    return 'This is going to be my home page'


@app.route('/cart', methods=['POST'])
def create_cart():
    cart = models.Cart()
    db.session.add(cart)
    db.session.commit()
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