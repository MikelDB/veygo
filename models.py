from app import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=False, unique=False)

    elements = db.relationship('Element', backref='cart', lazy='dynamic')
    discounts = db.relationship('Discount', backref='cart', lazy='dynamic')


    def __repr__(self):
        return '<Cart {}>'.format(self.id)


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, index=False, unique=False)
    name = db.Column(db.String(64), index=False, unique=False)

    def __repr__(self):
        return '<Element {}>'.format(self.id)


class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=False, unique=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    percentage = db.Column(db.Integer, index=False, unique=False)
    decimals = db.Column(db.Integer, index=False, unique=False)

    def __repr__(self):
        return '<Discount {}>'.format(self.id)
