from dish import *
from customer import *
from order import *


def menu():
    print('1. View the menu: ')
    print('2. Place orders: ')
    print('3. View order history and bill: ')
    print('4. Exit: ')


menu()
while True:

    choice = int(input('Choice: '))
    if choice == 1:
        print('1. Appetizers: ')
        print('2. Salads: ')
        print('3. Pizzas: ')
        print('4. All menu: ')
        which = int(input('Which one: '))
        if which == 1:
            print(Appetizers.appetizers)
        if which == 2:
            print(Salads.salads)
        if which == 3:
            print(Pizza.pizzas)
        elif which == 4:
            print(Dish.menu)
    elif choice == 2:
        name = input('Enter your name: ')
        contact = input('Your contact: ')
        cust = Customer(name, contact)
        orders = input('Enter your orders: ')
        dishes = [dish.strip() for dish in orders.split(',')]
        order1 = Orders(cust, *dishes)
        print(order1.place_order())

    elif choice == 3:
        name = input('Your name: ')
        print(order1.view_history(name))

    elif choice == 4:
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid input. Please enter a number between 1 and 4.')

