from lib.dishes import *

class Menu:
    def __init__(self, dishes):
        self.menu = dishes
    
    def see_all_dishes(self):
        menu = {}
        for dish in self.menu:
            menu[dish.name] = dish.price
        return menu
    
    def see_available_dishes(self):
        menu = {}
        for dish in self.menu:
            if dish.availability == 'Available':
                menu[dish.name] = dish.price
        return menu