from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name= name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"\n\t'{employee.name}' Added!")

    def view_employee(self):
        print("\n\tEmployee List: ")
        print("\t----------------------")
        for emp in self.employees:
            print(f"\tName: {emp.name}\n\tEmail: {emp.email}\n\tAddress: {emp.address}\n\tAge: {emp.age}\n\tDesignation: {emp.designation}\n\tSalary: {emp.salary}")
            print("\t-------------------|")