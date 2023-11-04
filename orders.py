from dishes import Dish


class Order:
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

    
    def __iadd__(self, other):
        if isinstance(other, Dish):
            self.add_item(other)
            return self
        else:
            raise TypeError("Додавання підтримується лише для об'єктів класу Dish.")