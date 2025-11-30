class A:
    """Class A"""
    name = "class A is a parent"
    is_main_class = True

    def print_hello(self):
        print("hello from A")

class B(A):
    """Class B"""
    name_b = "class B is a child"
    is_main_class = False

    def print_hello(self):
        print("hello from A")

class C(A):
    """Class C"""
    pass




class Vehicle:
    """It`s a base class for Vehicles"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def move(self):
        print("Your vehicle is moving")

class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, cost = 0) -> None:
        super().__init__(type, color)
        self.cost = cost

    def start_engine(self):
        print(f"Your car: {self.type, self.color, self.cost} is starting... Wrom Wrom")


class Bicycle(Vehicle):
    """Class Bicycle"""
    """Class Bicycle"""

    def __init__(self, type, color, count_of_wheels) -> None:
        super().__init__(type, color)
        self.count_of_wheels = count_of_wheels

    def runYourBicycle(self):
        print("You are so fast!!")

class Rower(Bicycle, Car):
    """Class Rower"""

    def __init__(self, type, color, count_of_wheels, number_of_brain = 0) -> None:
        super().__init__(type, color, count_of_wheels)
        self.number_of_brain = number_of_brain


rower = Rower("rower", "red", 2, 23)
rower.move()
rower.runYourBicycle()