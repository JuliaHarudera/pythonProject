class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        dish_list = "\n".join([str(dish) for dish in self.dishes])
        return f"{self.name}:\n{dish_list}"

    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, index):
        return self.dishes[index]

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.dishes):
            item = self.dishes(self.current_index)
            self.current_index = + 1
            return item
        else:
            raise StopIteration

