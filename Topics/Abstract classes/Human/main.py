from abc import ABC, abstractmethod


# create Human
class Human(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_hello(self):
        ...
