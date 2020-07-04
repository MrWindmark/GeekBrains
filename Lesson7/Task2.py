from abc import ABC, abstractmethod

# Переделал задание с учётом абстракций, так работать с объектами стало реально удобнее
# Спасибо)
class Clothes(ABC):

    @property
    @abstractmethod
    def clt_math_cons(self):
        pass

    @property
    @abstractmethod
    def clt_param(self):
        pass

    def prt(self):
        print(f'Params: {self.clt_param} value {self.clt_math_cons}')


class Coat(Clothes):

    def __init__(self, name, size):
        self.name = name
        self.__size = size

    @property
    def clt_math_cons(self):
        return self.__size / 6.5 + 0.5

    @property
    def clt_param(self):
        return self.name, self.__size


class Suit(Clothes):

    def __init__(self, name, size):
        self.name = name
        self.__size = size

    @property
    def clt_math_cons(self):
        return 2 * self.__size + 0.3

    @property
    def clt_param(self):
        return self.name, self.__size


test_coat1 = Coat('One', 19.5)
test_coat2 = Coat('Two', 13)
test_coat3 = Coat('Three', 32.5)
test_Suit1 = Suit('Again', 7)
test_Suit2 = Suit('And', 10)
test_Suit3 = Suit('End', 15)

test_coat1.prt()
test_coat2.prt()
test_coat3.prt()
test_Suit1.prt()
test_Suit2.prt()
test_Suit3.prt()
