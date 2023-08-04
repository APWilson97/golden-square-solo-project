from lib.order import *
from lib.menu import *
from lib.dishes import *
from lib.receipt import *
from lib.delivery import *
from datetime import datetime, timedelta

"""Given three dishes
We see those dishes reflected in a list with their prices"""

def test_show_list_of_three_dishes():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    assert menu.see_all_dishes() == {'Katsu Curry': 9.99, 'Kitsune Udon': 5.99, 'Tonkotsu Ramen': 7.99}

"""Given three dishes, with only two available
We see only the available dishes reflected in a list with their prices"""

def test_show_list_of_available_dishes():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Not Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    menu.see_available_dishes() == {'Katsu Curry': 9.99, 'Tonkotsu Ramen': 7.99}

"""Given three dishes in a menu
We can see a list of those dishes when they are added to an order"""

def test_see_order_of_three_dishes_added():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    assert order.see_all() == f"Your order list:\nKatsu Curry: 9.99\nKitsune Udon: 5.99\nTonkotsu Ramen: 7.99"

"""Given 3 dishes added to an order
We can see a correct list of orders when an order is removed from it"""

def test_add_three_remove_one_order_see_list():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    order.remove(dish2)
    assert order.see_all() == f"Your order list:\nKatsu Curry: 9.99\nTonkotsu Ramen: 7.99"

"""Given three dishes added to an order
We can see that the order is confirmed once we call the appropriate function on it"""

def test_order_is_confirmed():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    order.confirm_order()
    assert order.confirmed == True

"""Given three dishes added to an order
We can confirmed the contact details associated to an order once the appropriate function is called"""

def test_contact_details_entered_correctly():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    order.confirm_order()
    order.contact_details('Alex Wilson', '12345678911')
    assert order.customer_details == ['Alex Wilson', '12345678911']

"""Given three dishes added to an order
We can see the grand total of that order with the dish names and prices, as well as a total price"""

def test_see_itemised_receipt_total():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    receipt = Receipt(order)
    receipt.see_total() == f"Your order list:\nKatsu Curry: 9.99\nKitsune Udon: 5.99\nTonkotsu Ramen: 7.99\nTotal: 17.97"

"""Given an order
We can see if it is confirmed or not"""
def test_checking_if_order_is_confirmed_before_text():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    delivery = Delivery(order)
    assert delivery.send_text() == 'Please confirm your order first'

""" Given an order that is confirmed
We can send a text to the contact about when their order will be delivered """

def test_successfully_send_delivery_text():
    time_now = datetime.now()
    delivery_time = time_now + timedelta(minutes = 30)
    time_now_string = time_now.strftime("%H:%M")
    delivery_time_string = delivery_time.strftime("%H:%M")

    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
    dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
    menu = Menu([dish1, dish2, dish3])
    order = Order()
    order.add(dish1)
    order.add(dish2)
    order.add(dish3)
    order.confirm_order()
    delivery = Delivery(order)
    assert delivery.send_text() == f"Thank you! Your order was placed and it will be delivered before {delivery_time_string}"