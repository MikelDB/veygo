from app import app, models, db
from app.datatransformers import transformCartToJSON, transformOrderToJSON, transformProductsToJSON, transformCartElementsToOrderElements
from app.calculators import calculateTotalPriceFromCart
from flask import request, render_template
import uuid

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cart', methods=['POST'])
def create_cart():
    code = uuid.uuid1()
    cart = models.Cart(code=str(code))
    db.session.add(cart)
    db.session.commit()
    return transformCartToJSON(cart)


@app.route('/cart/<code>', methods=['GET'])
def get_cart(code):
    cart = models.Cart.query.filter(models.Cart.code == code).first()

    if cart is None:
        code = uuid.uuid1()
        cart = models.Cart(code=str(code))
        db.session.add(cart)
        db.session.commit()

    return transformCartToJSON(cart)


@app.route('/cart/<code>', methods=['DELETE'])
def delete_cart(code):
    cart = models.Cart.query.filter(models.Cart.code == code).first()
    db.session.delete(cart)
    db.session.commit()

    code = uuid.uuid1()
    cart = models.Cart(code=str(code))
    db.session.add(cart)
    db.session.commit()
    return transformCartToJSON(cart)


@app.route('/cart/<code>', methods=['POST'])
def add_item(code):
    element_code = uuid.uuid1()
    cart = models.Cart.query.filter(models.Cart.code == code).first()
    product = models.Product.query.filter(models.Product.reference == request.get_json()['reference']).first()
    element = models.Element(cart_id=code, product_id=product.id, code=str(element_code))

    cart.elements.append(element)
    db.session.commit()
    return transformCartToJSON(cart)


@app.route('/cart/<cart_code>/<element_code>', methods=['DELETE'])
def delete_item(cart_code, element_code):
    element = models.Element.query.filter(models.Element.code == element_code).first()
    db.session.delete(element)
    db.session.commit()

    cart = models.Cart.query.filter(models.Cart.code == cart_code).first()
    return transformCartToJSON(cart)


@app.route('/cart/<cart_code>/discount/<discount_code>', methods=['POST'])
def add_discount(cart_code, discount_code):
    error = {}
    cart = models.Cart.query.filter(models.Cart.code == cart_code).first()
    discount = models.Discount.query.filter(models.Discount.code == discount_code).filter(
        models.Discount.cart_id == None).filter(models.Discount.order_id == None).first()

    if discount is not None:
        cart.discounts.append(discount)
        db.session.commit()
    else:
        error = {
            'code': 1,
            'message': 'Code do not exist or has already been used'
        }

    return transformCartToJSON(cart, error)


@app.route('/cart/<cart_code>/checkout', methods=['GET'])
def checkout(cart_code):
    cart = models.Cart.query.filter(models.Cart.code == cart_code).first()
    order_code = uuid.uuid1()
    order = models.Order(
        code=str(order_code),
        final_price=calculateTotalPriceFromCart(cart),
        elements=transformCartElementsToOrderElements(cart.elements, order_code),
        discounts=cart.discounts,
        final_price_decimals=2
    )
    cart.checked_out = True
    db.session.add(order)
    db.session.commit()

    return {
        'code': order_code
    }


@app.route('/order/<order_code>', methods=['GET'])
def get_orders(order_code):
    order = models.Order.query.filter(models.Order.code == order_code).first()

    return transformOrderToJSON(order)


@app.route('/product', methods=['GET'])
def get_products():
    products = models.Product.query.all()

    return transformProductsToJSON(products)
