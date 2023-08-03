from lib.dishes import Dishes

class Order:
    def __init__(self):
        self.order_list = []
        self.customer_details = []
        self.confirmed = False
    
    def add(self, dish):
        if dish.availability == 'Available':
            self.order_list.append(dish)
        else:
            return 'Sorry, this dish is not available today. Please select another dish'
    
    def remove(self, dish):
        self.order_list.remove(dish)
    
    def see_all(self):
        final_order_string = f"Your order list:\n"
        for dishes in self.order_list:
            final_order_string += f"{dishes.name}: {dishes.price}\n"
        print(final_order_string)
        return final_order_string.strip()
    
    def list_orders(self):
        return self.order_list
    
    def confirm_order(self):
        self.confirmed = True
    
    def contact_details(self, name, phone_number):
        self.customer_details = [name, phone_number]
    

    