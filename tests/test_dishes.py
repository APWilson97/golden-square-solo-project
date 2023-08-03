from lib.dishes import *

"""Given a dish
Check that its properties are set correctly"""

def test_dish_properties_set_correctly():
    dish1 = Dishes('Katsu Curry', 9.99, 'Available')
    assert dish1.name == 'Katsu Curry'
    assert dish1.price == 9.99
    assert dish1.availability == 'Available'