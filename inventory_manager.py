class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        self.products[name] = quantity

    def get_stock(self, name):
        return self.products.get(name, 0)
