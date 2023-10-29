import logging
from dishes import Dish
from Menu import MenuCategory
from orders import Order
from discounts import RegularDiscount, SilverDiscount, GoldDiscount
from clients import Client

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
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