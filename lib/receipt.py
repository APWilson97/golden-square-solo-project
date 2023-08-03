from lib.order import Order

class Receipt:
    def __init__(self, order):
        self.order = order
    
    def calculate_total(self):
        total = []
        for dish in self.order.list_orders():
            total.append(dish.price)
        return sum(total)
    
    def see_total(self):
        total_string_end = f"\nTotal: {self.calculate_total()}"
        return self.order.see_all() + total_string_end