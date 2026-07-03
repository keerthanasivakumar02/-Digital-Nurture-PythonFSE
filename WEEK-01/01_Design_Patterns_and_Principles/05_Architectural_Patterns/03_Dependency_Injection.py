# Dependency Injection (DI) Pattern

from abc import ABC, abstractmethod


class PaymentService(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(PaymentService):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PaymentApp:

    def __init__(self, payment_service):
        self.payment_service = payment_service

    def make_payment(self, amount):
        self.payment_service.pay(amount)


upi = UPIPayment()
app = PaymentApp(upi)

app.make_payment(500)