class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_stock(self, name, qty):
        available = self.stock.get(name, 0)
        if qty > available:
            raise ValueError("not enough stock")
        self.stock[name] = available - qty