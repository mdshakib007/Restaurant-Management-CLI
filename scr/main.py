from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from users import Customer, Admin, Employee


AlgoRestaurant = Restaurant("Algo-Restaurent")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    customer = Customer(name= name, email= email, address= address)

    while True:
        print(f"\n-------{customer.name} as customer of {AlgoRestaurant.name}------")
        print("Navigate to: ")
        print("1. Show Menu")
        print("2. Add to Cart")
        print("3. My Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        op = input(">>> ")

        if op == "1":
            customer.view_menu(AlgoRestaurant)
            
        elif op == "2":
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(restaurant= AlgoRestaurant, item_name= item_name, quantity= item_quantity)

        elif op == "3":
            customer.view_cart()

        elif op == "4":
            customer.pay_bill()

        elif op == "5":
            break

        else:
            print("Invalid input!")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    admin = Admin(name= name, email= email, address= address)

    while True:
        print(f"\n-------{admin.name} as admin of {AlgoRestaurant.name}------")
        print("Navigate to: ")
        print("1. Show Menu")
        print("2. Add Menu Item")
        print("3. Add New Employee")
        print("4. Employee List")
        print("5. Delete Item")
        print("6. Exit")
        
        op = input(">>> ")

        if op == "1":
            admin.show_items(AlgoRestaurant)

        elif op == "2":
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quan = int(input("Enter item quantity: "))

            item = FoodItem(name= item_name , price= item_price, quantity= item_quan)
            admin.add_new_item(AlgoRestaurant, item= item)

        elif op == "3":
            emp_name = input("Enter employee name: ")
            emp_email = input("Enter employee email: ")
            emp_address = input("Enter employee address: ")
            emp_age = int(input("Enter employee age: "))
            emp_desig = input("Enter employee designation: ")
            emp_salary = int(input("Enter employee salary: "))

            employee = Employee(name= emp_name, email= emp_email, address= emp_address, age= emp_age, designation= emp_desig, salary= emp_salary)
            admin.add_employee(AlgoRestaurant, employee= employee)

        elif op == "4":
            admin.view_employee(AlgoRestaurant)
        
        elif op == "5":
            item_name = input("Enter item name: ")
            admin.remove_item(AlgoRestaurant, item= item_name)

        elif op == "6":
            break

        else:
            print("Invalid input!")


while True:

    print(f"\n------Welcome to {AlgoRestaurant.name}-------")
    print("Navigate to:")
    print("1. Customer Login")
    print("2. Admin Login")
    print("3. Exit")

    op = input(">>> ")

    if op == "1":
        customer_menu()
    elif op == "2":
        admin_menu()
    elif op == "3":
        break
    else:
        print("Invalid input!")
