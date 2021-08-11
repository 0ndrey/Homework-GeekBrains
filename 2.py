from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def using(self):
        pass


class Coat(Cloth):
    def __init__(self, V):
        self.V = V

    @property
    def using(self):
        return self.V / 6.5 + 0.5


class Jacket(Cloth):
    def __init__(self, H):
        self.H = H

    @property
    def using(self):
        return self.H * 2 + 0.3


coat = Coat(20)
jacket = Jacket(1.7)
print(round(coat.using, 2))
print(round(jacket.using, 2))