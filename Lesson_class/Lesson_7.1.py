class Counter:
    """Class Counter"""
    def __init__(self, count_obj, type_obj, max_elements):
        self.max_elements = max_elements
        self.count_obj = count_obj
        self.type_obj = type_obj

    def counter(self):
        print(f"Type: of object: {self.type_obj}")
        if isinstance(self.count_obj, (list, dict, str, tuple)):
            count = len(self.count_obj)
            if count > self.max_elements:
                print("Count elements of your object more than need")
                print(f"More on {count - self.max_elements}")
            else:
                print(f"Count of elements: {count}")
        else:
            print("Your object must be iterable")

    def get_atters(self):
        print(self.__dict__)

    def set_atters(self, attr, value):
        if hasattr(self, self.__dict__[attr]):
            setattr(self, self.__dict__[attr], value)
        else:
            print("Check your attrs")

class List_Elements(Counter):
    """Class for List_Elements"""
    def __init__(self, count_obj, type_obj, max_elements) -> None:
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()

        print("Operation was ended")

list_ex = List_Elements([1,2,3,4,5], list, 10)
list_ex.counter()