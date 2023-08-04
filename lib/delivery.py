from lib.order import *
from lib.send_sms import *
import os
from datetime import datetime, timedelta

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
            with open('/Users/alexanderwilson/Projects/golden_square/solo_project/lib/send_sms.py') as f:
                exec(f.read())
            time_now = datetime.now()
            delivery_time = time_now + timedelta(minutes = 30)
            time_now_string = time_now.strftime("%H:%M")
            delivery_time_string = delivery_time.strftime("%H:%M")
            return f"Thank you! Your order was placed and it will be delivered before {delivery_time_string}"
        else:
            return 'Please confirm your order first'
        
    
