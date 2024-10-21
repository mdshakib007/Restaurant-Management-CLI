from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if item.quantity < quantity:
                print(f"\n\tNot enough '{item_name}' to add into the cart!")
            else:
                prev_quantity = item.quantity
                item.quantity = quantity
                self.cart.add_item(item)
                item.quantity = (prev_quantity - quantity)
                restaurant.menu.add_menu_item(item)
                print(f"\n\t'{item_name}' X{quantity} added to the cart!")
        else:
            print(f"\n\t'{item_name}' not found!")
    
    def view_cart(self):
        print("\n\t-------Cart-------")
        print("\tName\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"\t{item.name}\t{item.price}\t{quantity}")
        print(f"\tTotal Price: {self.cart.total_price}")
        print("\t--------------------|")

    def pay_bill(self):
        if self.cart.total_price == 0:
            print("\n\tYour cart is empty!")
        else:
            print(f"\n\tTotal ${self.cart.total_price} paid successfully!")
            self.cart.clear_cart()



class Employee(User):
    def __init__(self, name, email, address, salary, designation, age):
        super().__init__(name, email, address)
        self.salary = salary
        self.designation = designation
        self.age = age


class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
    
    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_menu_item(item)

    def show_items(self, restaurant):
        restaurant.menu.show_menu()
    
