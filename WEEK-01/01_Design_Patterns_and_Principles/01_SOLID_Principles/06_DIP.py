# Dependency Inversion Principle (DIP)

from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):

    def send(self, message):
        print("SMS:", message)


class AlertService:

    def __init__(self, notification):
        self.notification = notification

    def notify(self, message):
        self.notification.send(message)


email = EmailNotification()
service = AlertService(email)

service.notify("Your order has been placed successfully.")