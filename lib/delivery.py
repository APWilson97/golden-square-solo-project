from lib.order import *

class Delivery:
    def __init__(self, order):
        self.order = order
    
    def is_order_confirmed(self):
        if self.order.confirmed == True:
            return True
        else:
            return False

    def send_text(self):
        if self.is_order_confirmed():
            return 'Thanks for your order!'
        else:
            return 'Please confirm your order first'
