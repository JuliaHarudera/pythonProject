from discounts import Discount

class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total = order.calculate_total()
        discounted_total = self.discount.discount(total)
        return discounted_total
