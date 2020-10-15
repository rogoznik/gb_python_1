from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


coat = Coat('coat', 7)
suit = Suit('suit', 1.75)
print(coat.tissue_consumption)
print(suit.tissue_consumption)
print(coat.tissue_consumption + suit.tissue_consumption)
