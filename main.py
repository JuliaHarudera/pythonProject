class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price:.2f}"

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        dish_list = "\n".join([str(dish) for dish in self.dishes])
        return f"{self.name}:\n{dish_list}"

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

class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total = order.calculate_total()
        discounted_total = self.discount.discount(total)
        return discounted_total


dish1 = Dish("Салат Цезар", "З куркою та соусом", 10.99)
dish2 = Dish("Паста Карбонара", "З беконом та пармезаном", 12.99)
dish3 = Dish("Тірамісу", "Італійський десерт", 5.99)


category1 = MenuCategory("Закуски", [dish1])
category2 = MenuCategory("Основні страви", [dish2])
category3 = MenuCategory("Десерти", [dish3])


order = Order()
order.add_item(dish1)
order.add_item(dish2)
order.add_item(dish3)


client_regular = Client("Dima", RegularDiscount())
client_silver = Client("Oleh", SilverDiscount())
client_gold = Client("Ivan", GoldDiscount())


total_regular = client_regular.get_total_price(order)
total_silver = client_silver.get_total_price(order)
total_gold = client_gold.get_total_price(order)


print("Меню ресторану:")
print(category1)
print(category2)
print(category3)
print("\nЗамовлення:")
for item in order.items:
    print(item)
print("\nРозрахунок для клієнтів:")
print(f"{client_regular.name}: Загальна вартість замовлення: ${total_regular:.2f}")
print(f"{client_silver.name}: Загальна вартість замовлення: ${total_silver:.2f}")
print(f"{client_gold.name}: Загальна вартість замовлення: ${total_gold:.2f}")
