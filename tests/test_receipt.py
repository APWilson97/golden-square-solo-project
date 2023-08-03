from lib.receipt import *
from lib.order import *
from unittest.mock import Mock

def test_calculate_total():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Available')
    order = Order()
    order.add(dish1)
    order.add(dish2)
    receipt = Receipt(order)
    assert receipt.calculate_total() == 18.98

def test_see_total():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Tonkotsu Ramen', 8.99, 'Available')
    order = Order()
    order.add(dish1)
    order.add(dish2)
    receipt = Receipt(order)
    assert receipt.see_total() == f"Your order list:\nKatsu Curry: 9.99\nTonkotsu Ramen: 8.99\nTotal: 18.98"