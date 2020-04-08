def calculateTotalPriceFromCart(cart):
    total_price = 0
    for element in cart.elements:
        total_price += element.product.price

    for discount in cart.discounts:
        total_price -= total_price * (discount.percentage * 0.0001)
    return total_price
