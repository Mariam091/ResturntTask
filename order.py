from dish import *
from customer import *


class Orders:
    def __init__(self, customer: Customer, *dishes):
        self.customer = customer
        self.dishes = dishes
        self.total_price = 0

    orders = []

    def place_order(self):
        customer = str(self.customer)
        for dish in self.dishes:
            founder = False
            for k, v in Dish.menu.items():
                if dish in v:
                    self.total_price += int(v[dish].replace('֏', ''))
                    founder = True
                    break
            if not founder:
                return f"Error: Don't have {dish} in the menu"
        Orders.orders.append({customer: [self.dishes, self.total_price]})
        return f'Thank your for your order: '

    def view_history(self,name):
        for i in Orders.orders:
            if name in i:
                return f"Order History for {name}: {i[name]}"
        return 'Sorry: Your datas are incorrect: '




