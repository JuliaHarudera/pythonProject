class Discount:
    def discount(self, total):
        return total


class RegularDiscount(Discount):
    def discount(self, total):
        return total


class SilverDiscount(Discount):
    def discount(self, total):
        return total * 0.95  # 5% знижка для Silver


class GoldDiscount(Discount):
    def discount(self, total):
        return total * 0.90  # 10% знижка для Gold
