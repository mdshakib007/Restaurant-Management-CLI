class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # if the item already exists in the cart
        else:
            self.items[item] = item.quantity # if item is not in cart

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear_cart(self):
        self.items = {}
        print(f"\n\tNow the cart is empty!")
