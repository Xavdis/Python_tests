from abc import ABC, abstractmethod

class DiscountCalculator(ABC):
    @abstractmethod
    def get_discounted_product(self):
        pass

class DiscountCalculatorShirt(DiscountCalculator):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.10)


class DiscountCalculatorTShirt(DiscountCalculator):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPant(DiscountCalculator):

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.35)

dc_shirt = DiscountCalculatorShirt(100)
dc_Tshirt = DiscountCalculatorTShirt(100)
dc_pants = DiscountCalculatorPant(100)

print(dc_shirt.get_discounted_product())
print(dc_Tshirt.get_discounted_product())
print(dc_pants.get_discounted_product())
