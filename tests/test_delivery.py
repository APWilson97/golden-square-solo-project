from lib.delivery import *

def test_delivery_is_set_to_order():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Available')
    order = Order()
    order.add(dish1)
    order.add(dish2)
    delivery = Delivery(order)
    assert delivery.order == order

def test_order_confirmation_is_checked():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Available')
    order = Order()
    order.add(dish1)
    order.add(dish2)
    delivery = Delivery(order)
    assert delivery.send_text() == 'Please confirm your order first'

