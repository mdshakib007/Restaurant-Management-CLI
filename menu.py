class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        found = False
        for _item in self.items:
            if _item.name == item.name:
                self.items.remove(_item)
                found = True
        self.items.append(item)
        if not found:
            print(f"\n\t'{item.name}' added into menu!")
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower()  == item_name.lower():
                return item
        return None
    
    def remove_menu_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"\n\t'{item_name}' deleted!")
        else:
            print(f"\n\t'{item_name}' is not found!")
    
    def show_menu(self):
        print("\n\t---------Menu----------")
        print(f"\tName\tPrice\tQuantity")
        for item in self.items:
            print(f"\t{item.name}\t{item.price}\t{item.quantity}")
