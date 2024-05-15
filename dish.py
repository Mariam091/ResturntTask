class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    menu = {}


class Appetizers(Dish):
    appetizers = {'Mista': '7200֏',
                  'Meat assortment': '4500֏',
                  'Cheese assortment': '4500֏',
                  'Fish bruschetta': '4200֏',
                  'Bruschetta mix': '2700֏'
                  }
    Dish.menu['Appetizers'] = appetizers


class Salads(Dish):
    salads = {'Tomato mozzarella': '2900֏',
              'Sea salad': '4900֏',
              'Cesar': '3400֏',
              'Quinoa chicken': '4500֏',
              'Burratini': '5500֏'
              }
    Dish.menu['Salads'] = salads


class Pizza(Dish):
    pizzas = {'Academia Italia': '4200֏',
              'Prosciutto': '4200֏',
              'With salmon': '4700֏',
              'Mortadella ricotta': '4400֏'
              }
    Dish.menu['Pizzas'] = pizzas


