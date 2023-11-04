class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def __iadd__(self, other_cart):
        if isinstance(other_cart, Cart):
            self.items += other_cart.items
            return self
        else:
            raise TypeError("Додавання підтримується лише для об'єктів класу Cart.")