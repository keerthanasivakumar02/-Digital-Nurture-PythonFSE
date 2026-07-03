# Decorator Pattern
# Adds extra features to an object.

class IceCream:

    def price(self):
        return 50


class ChocolateDecorator:

    def __init__(self, icecream):
        self.icecream = icecream

    def price(self):
        return self.icecream.price() + 30


icecream = IceCream()
choco_icecream = ChocolateDecorator(icecream)

print("Total Price:", choco_icecream.price())