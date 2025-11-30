class BaseInetface:
    """Class BaseInetface"""
    def __init__(self, high, width, color):
        self.high = high
        self.width = width
        self.color = color

    def get_one_atters(self, attr):
        pass
    def print_model(self) -> None:
        pass
    def count_of_price(self) -> None:
        pass

class GetOneAtters(BaseInetface):
    """Class Get_One_atters"""
    def get_one_atters(self, attr):
        getattr(self.__dict__[attr], attr)

intr_1 = BaseInetface(high=111, width=23, color='red')
attr = intr_1.get_one_atters("high")

intr_2 = GetOneAtters(141, 3, 'black')
print(getattr(intr_2, "high"))



class BaseInetface:
    """Class BaseInetface"""
    def __init__(self, high, width, color):
        self.high = high
        self.width = width
        self.color = color

    def get_one_attr(self, attr):
        return getattr(self, attr)

my_interface = BaseInetface(100, 50, "red")

print(my_interface.get_one_attr("width"))