class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        dish_list = "\n".join([str(dish) for dish in self.dishes])
        return f"{self.name}:\n{dish_list}"