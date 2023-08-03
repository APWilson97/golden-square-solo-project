from lib.menu import *
from unittest.mock import Mock

def test_menu_contains_dishes():
    fakedish1 = Mock()
    fakedish1.name = 'name'
    fakedish1.price = 'price'
    menu = Menu([fakedish1])
    assert menu.menu == [fakedish1]

def test_see_all_dishes_properties_correctly():
    fakedish1 = Mock()
    fakedish1.name = 'name'
    fakedish1.price = 'price'
    menu = Menu([fakedish1])
    assert menu.see_all_dishes() == {'name': 'price'}

def test_see_all_available_dishes_correctly():
    fakedish1 = Mock()
    fakedish1.name = 'name'
    fakedish1.price = 'price'
    fakedish1.availability = 'Not Available'
    fakedish2 = Mock()
    fakedish2.name = 'name2'
    fakedish2.price = 'price2'
    fakedish2.availability = 'Available'
    menu = Menu([fakedish1, fakedish2])
    assert menu.see_available_dishes() == {'name2': 'price2'}