# Factory Method Pattern

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Dog says: Bark"


class Cat(Animal):

    def sound(self):
        return "Cat says: Meow"


class AnimalFactory:

    @staticmethod
    def create_animal(choice):

        if choice.lower() == "dog":
            return Dog()

        elif choice.lower() == "cat":
            return Cat()

        else:
            return None


animal = AnimalFactory.create_animal("dog")

print(animal.sound())