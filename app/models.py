from . import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(36), index=False, unique=True)
    checked_out = db.Column(db.Boolean, index=False, unique=True)

    elements = db.relationship('Element', backref='cart', lazy='dynamic', cascade="all, delete-orphan")
    discounts = db.relationship('Discount', backref='cart', lazy='dynamic')

    def __repr__(self):
        return '<Cart {}>'.format(self.id)


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(36), index=False, unique=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    product = db.relationship("Product")

    def __repr__(self):
        return '<Element {}>'.format(self.id)


class OrderElement(db.Model):
    __tablename__ = 'order_element'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(36), index=False, unique=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    product = db.relationship("Product")

    def __repr__(self):
        return '<Element {}>'.format(self.id)


class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=False, unique=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    percentage = db.Column(db.Integer, index=False, unique=False)
    decimals = db.Column(db.Integer, index=False, unique=False)

    def __repr__(self):
        return '<Discount {}>'.format(self.id)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(20), index=False, unique=True)
    name = db.Column(db.String(20), db.ForeignKey('cart.id'))
    price = db.Column(db.Integer, index=False, unique=False)
    decimals = db.Column(db.Integer, index=False, unique=False)

    def __repr__(self):
        return '<Product {}>'.format(self.id)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(36), index=False, unique=True)
    final_price = db.Column(db.Integer, index=False, unique=False)
    final_price_decimals = db.Column(db.Integer, index=False, unique=False)

    elements = db.relationship('OrderElement', backref='order', lazy='dynamic', cascade="all, delete-orphan")
    discounts = db.relationship('Discount', backref='order', lazy='dynamic')

    def __repr__(self):
        return '<Cart {}>'.format(self.id)