from lib.order import *

def test_order_properties_set_correctly():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Available')
    order = Order()
    order.add(dish1)
    order.add(dish2)
    assert order.see_all() == f"Your order list:\nKatsu Curry: 9.99\nTonkotsu Ramen: 8.99"

def test_add_unavailable_order():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Not Available')
    order = Order()
    order.add(dish1)
    assert order.add(dish2) == 'Sorry, this dish is not available today. Please select another dish'
    