from sympy import false


class Person:
    """Class for creating a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attrs(self):
        print(self.name, self.age)


per1 = Person("Taomi", 54)
per1.print_attrs()
per2 = Person("Nanami", 22)
per2.print_attrs()


class Point:
    """Class for creating a point"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attr()
        self.check_coords()

    def check_coords(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0:
                print("Coord can`t be less than 0")
                setattr(self, attr, 0)
            elif getattr(self,attr, False)>100:
                print("Coord can`t be greater than 100")
                setattr(self, attr, 100)
        print(self.__dict__)

    def get_attr(self):
        print(self.__dict__)

    def set_attr(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print(self.__dict__)

coord_1 = Point(-1,101,50)

coord_2 = Point(1001,1010,-5)
print(getattr(coord_2, "x", False))