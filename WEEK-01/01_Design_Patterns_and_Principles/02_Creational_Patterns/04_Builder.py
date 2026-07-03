# Builder Pattern

class Pizza:

    def __init__(self):
        self.size = ""
        self.topping = ""

    def display(self):
        print("Pizza Size:", self.size)
        print("Topping:", self.topping)


class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_topping(self, topping):
        self.pizza.topping = topping
        return self

    def build(self):
        return self.pizza


pizza = (
    PizzaBuilder()
    .set_size("Large")
    .set_topping("Cheese")
    .build()
)

pizza.display()