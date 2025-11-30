from abc import ABC, abstractmethod

class Car(ABC):

    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractmethod
    def car_preview(self):
        pass

class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs: {self.cost}")


class Mercedes(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs: {self.cost}")

class BMW(Car):
    pass

toyota = Toyota("off-road", 1200)
toyota.car_preview()


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Cat(Animal):
    def __init__(self, color, age) -> None:
        self.color = color
        self.age = age

    def move(self):
        print(f"Cat with {self.color} color go ahead.")

    def eat(self):
        print(f"Cat ate this food for {self.age} years.")


class Dog(Animal):
    def __init__(self, color, age, eyes_color) -> None:
        self.color = color
        self.age = age
        self.eyes_color = eyes_color

    def move(self):
        print(f"Dog with {self.color} color and {self.eyes_color}go ahead.")

    def eat(self):
        print(f"Dog ate this food for {self.age} years.")

class AnimalType(Animal):
    pass

class Bird(AnimalType):
    def __init__(self, name) -> None:
        self.name = name

    def move(self):
        print(f"Bird {self.name} fly.")

    def eat(self):
        print(f"Bird {self.name} eat.")