from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def evaluate_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    @property
    def evaluate_consumption(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    @property
    def evaluate_consumption(self):
        return 2 * self.__height + 0.3


coat = Coat('My the warmest coat', 14)
costume = Costume('My official costume', 179)

print(f'For crafting {coat.name} will be needed {coat.evaluate_consumption} of material')
print(f'For crafting {costume.name} will be needed {costume.evaluate_consumption} of material')
