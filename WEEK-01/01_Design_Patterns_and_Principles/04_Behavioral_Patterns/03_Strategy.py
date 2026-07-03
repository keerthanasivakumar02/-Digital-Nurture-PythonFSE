# Strategy Pattern
# Selects a payment method at runtime.

class Cash:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


class DebitCard:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class Payment:

    def __init__(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)


payment = Payment(Cash())
payment.make_payment(1000)