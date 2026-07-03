# Interface Segregation Principle (ISP)

from abc import ABC, abstractmethod


class Camera(ABC):

    @abstractmethod
    def take_photo(self):
        pass


class MusicPlayer(ABC):

    @abstractmethod
    def play_music(self):
        pass


class Smartphone(Camera, MusicPlayer):

    def take_photo(self):
        print("Taking a photo.")

    def play_music(self):
        print("Playing music.")


phone = Smartphone()

phone.take_photo()
phone.play_music()