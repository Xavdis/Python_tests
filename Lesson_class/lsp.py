class Car:
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost):
        self.properties = {"Color": color, "Cost": cost}

    def get_properties(self):
        return self.properties

class PetrolCar(Car):
    pass

car = Car("Toyota")
car.set_properties("Red", 24444)

petrol_car = PetrolCar("Mercedes")
petrol_car.set_properties("Black", 23000)

cars = [car, petrol_car]

def get_count_of_colors(color):
    count = 0
    for car in cars:
        if car.properties["Color"] == color:
            count += 1
    print(count)

get_count_of_colors("Black")


