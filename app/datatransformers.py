import uuid
from app import models


def transformCartToJSON(cart, error={}):
    cart_json = {
        'code': cart.code,
        'elements': [],
        'discounts': [],
        'error': error
    }

    for element in cart.elements:
        cart_json['elements'].append({
            'code': element.code,
            'product': {
                'reference': element.product.reference,
                'name': element.product.name,
                'price': element.product.price,
                'decimals': element.product.decimals
            }
        })

    for discount in cart.discounts:
        cart_json['discounts'].append({
            'code': discount.code,
            'percentage': discount.percentage,
            'decimals': discount.decimals
        })

    return cart_json


def transformOrderToJSON(order, error={}):
    order_json = {
        'code': order.code,
        'finalPrice': order.final_price,
        'finalPriceDecimals': order.final_price_decimals,
        'elements': [],
        'discounts': [],
        'error': error
    }

    for element in order.elements:
        order_json['elements'].append({
            'code': element.code,
            'product': {
                'reference': element.product.reference,
                'name': element.product.name,
                'price': element.product.price,
                'decimals': element.product.decimals
            }
        })

    for discount in order.discounts:
        order_json['discounts'].append({
            'code': discount.code,
            'percentage': discount.percentage,
            'decimals': discount.decimals
        })

    return order_json


def transformProductsToJSON(products):
    products_json = {
        'products': []
    }

    for product in products:
        products_json['products'].append({
            'reference': product.reference,
            'name': product.name,
            'price': product.price,
            'decimals': product.decimals
        })

    return products_json


def transformCartElementsToOrderElements(elements, order_code):
    order_elements = []
    for element in elements:
        order_element_code = uuid.uuid1()
        order_elements.append(
            models.OrderElement(
                code=str(order_element_code),
                order_id=str(order_code),
                product_id=element.product_id
            )
        )

    return order_elements