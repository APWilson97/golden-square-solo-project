Describe the problem:

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

Design the Class System:
Nouns:
list of dishes
prices
meal
number of dishes
receipt with grand total
order
text

Verbs:
check
order
see a list
select
verify
see itemised receipt
receive a text

Classes:
Menu
Order
Dishes
Receipt
Delivery
                          ┌───────────────────────────┐
                          │ Menu:                     │
                          │ see_all_dishes()          │
                          │ available_dishes()        │
                          │                           │         ┌─────────────────────────┐
                          │                           │         │ Dishes:                 │
                          │                           │◄────────┤ is_available()          │
                          │                           │         │                         │
                          │                           │         │                         │
                          │                           │         │                         │
                          └─────┬────────────▲────────┘         └─────────────────────────┘
                                │            │
                                │            │
┌────────────────────┐     ┌────▼────────────┴───────┐
│ Delivery:          │     │ Order:                  │       ┌─────────────────────────────┐
│ send_text()        ├────►│ add()                   │◄──────┤ Receipt:                    │
│                    │     │ see_all()               │       │ see_total()                 │
│                    │     │ remove()                │       │                             │
│                    │◄────┤ contact_details()       ├──────►│                             │
│                    │     │                         │       │                             │
│                    │     │                         │       │                             │
└────────────────────┘     └─────────────────────────┘       └─────────────────────────────┘

Design of Class Interface in more detail:
class Menu:
    def __init__(self, list):
        # self.list - list
        # list of all the dishes
    
    def see_all_dishes(self):
        # return a list of all dishes with their prices
    
    def see_available_dishes(self)
        # return a list of dishes in stock and available
    
    
class Order:
    Public Properties:
        orders: a list of current orders
    
    def __init__(self):
        # list of orders - empty list
        # customer details - empty list
        # self.confirmed = False
    
    def add(self, dish):
        # Parameters:
        #   dish - Dishes object
        # Side Effects:
        #   Adds dish to list of orders if it is available
        #   Return a message saying if it is not and don't add anything
    
    def see_all(self):
        # returns list of orders and also prints it out for the user
    
    def remove(self, dish):
        # Parameters:
        #   dish - Dishes object
        # Side Effects:
        #   Removes dish from list of orders
    
    def contact_details(self, name, phone_number):
        # Parameters:
        #   name - string of name
        #   phone_number - string of their phone number
        # Side Effects:
        #   adds details to customer details
    
    def confirm_order(self):
        # Side Effects:
        #   Set confirmed property to True
    
class Receipt:
    def __init__(self, order):
        self.order = order

    def see_total(self):
        # Returns an integer of the sum
        # of all the dish prices
        # in the order

class Delivery:
    def __init__(self, order):
        self.order = order

    def is_order_confirmed(self, order):
        # Parameters:
        #   Instance of Order class
        # Checks if the order is confirmed or not
    
    def send_text(self, order):
        # Parameters:
        #   Instance of Order class
        # Check if order is confirmed
        # If true, then send text to customer
        # If false, remind customer to confirm order

class Dishes:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability (string)
    

Integration Tests:
"""Given three dishes
We see those dishes reflected in a list with their prices"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
menu.see_all_dishes() == {'Katsu Curry': 9.99, 'Kitsune Udon': 5.99, 'Tonkotsu Ramen': 7.99}

"""Given three dishes, with only two available
We see only the available dishes reflected in a list with their prices"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Not Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
menu.see_available_dishes() == {dish1.name: dish1.price, dish3.name: dish3.price}

"""Given three dishes in a menu
We can see a list of those dishes when they are added to an order"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
order = Order()
order.add(dish1)
order.add(dish2)
order.add(dish3)
order.see_all() == f"Your order list: {dish1.name: dish1.price, dish2.name: dish2.price, dish3.name: dish3.price}"

"""Given 3 dishes added to an order
We can see a correct list of orders when an order is removed from it"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
order = Order()
order.add(dish1)
order.add(dish2)
order.add(dish3)
order.remove(dish2)
order.see_all() == f"Your order list: {dish1.name: dish1.price, dish3.name: dish3.price}"

"""Given three dishes added to an order
We can see that the order is confirmed once we call the appropriate function on it"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
order = Order()
order.add(dish1)
order.add(dish2)
order.add(dish3)
order.confirm_order()
order.confirmed == True

"""Given three dishes added to an order
We can confirmed the contact details associated to an order once the appropriate function is called"""

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
order.customer_details == ['Alex Wilson', '12345678911']

"""Given three dishes added to an order
We can see the grand total of that order with the dish names and prices, as well as a total price"

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
order = Order()
order.add(dish1)
order.add(dish2)
order.add(dish3)
receipt = Receipt(order)
receipt.see_total() == f"Your order list: {dish1.name: dish1.price, dish2.name: dish2.price, dish3.name: dish3.price}
                        Total: 23.97"

"""Given an order
We can see if it is confirmed or not"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish2 = Dishes('Kitsune Udon', 5.99, 'Available')
dish3 = Dishes('Tonkotsu Ramen', 7.99, 'Available')
menu = Menu([dish1, dish2, dish3])
order = Order()
order.add(dish1)
order.add(dish2)
order.add(dish3)
delivery = Delivery(order)
delivery.send_text() == 'Please confirm your order first'

"""Given an order that is confirmed
We can send a text to the contact about when their order will be delivered"""

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
delivery.send_text() == f"Thank you! Your order was placed and it will be delivered before 12:30"


Unit Tests:
"""Given three dishes in a menu
We can see the dishes are properly set to the list property of the menu"""

dish1 = Mock()
dish2 = Mock()
dish3 = Mock()
menu = Menu([dish1, dish2, dish3])
menu.list = [dish1, dish2, dish3]

"""Given two dishes in a menu
We can see the dishes correctly displayed in the proper format"""

dish1 = Mock()
dish1.name = 'name'
dish1.price = 'price'
dish2 = Mock()
dish2.name = 'name2'
dish2.price 'price2'
menu = Menu([dish1, dish2])
menu.see_all_dishes() == {'name': 'price', 'name2': 'price2'}

"""Given two dishes in a menu
We can see which available dishes are correctly displayed"""

dish1 = Mock()
dish1.name = 'name'
dish1.price = 'price'
dish1.availability = 'Not Available'
dish2 = Mock()
dish2.name = 'name2'
dish2.price = 'price2'
dish2.availability = 'Available'
menu = Menu([dish1, dish2])
menu.see_available_dishes() == {'name2', 'price2'}

"""Given a dish
Check that its properties are set correctly"""

dish1 = Dishes('Katsu Curry', 9.99, 'Available')
dish1.name == 'Katsu Curry'
dish1.price == 9.99
dish1.availability == 'Available'

"""Given some orders
Check that the receipt reflects the total and the order list"""
dish1 = Mock()
dish1.name = 'name'
dish1.price = 'price'
dish2 = Mock()
dish2.name = 'name2'
dish2.price = 'price2'
order = Order()
order.add(dish1)
order.add(dish2)
receipt = Receipt(order)
receipt.see_total() == f"Your order: name, price, name2, price2
                        Your total: price1price2

"""Given two dishes
order correctly add them to its list"""

order = Order()
fakedish1 = Mock()
fakedish1.name = 'name'
fakedish1.price = 'price'
fakedish2 = Mock()
fakedish2.name = 'name'
fakedish2.price = 'price'
order.add(fakedish1)
order.add(fakedish2)
order.see_all() == f"Your order list: {'name': 'price', 'name2': 'price2'}

