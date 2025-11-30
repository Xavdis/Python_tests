class Card:
    """Class card for users card"""

    def __init__(self, card_number, balance) -> None:
        if self.__check_attribute(card_number, str):
            self._card_number = card_number
        if self.__check_attribute(balance, float):
            self.__balance = balance

    def get_card_data(self):
        return self.__dict__

    def set_card_data(self, attr, value):
        if type(attr) == str:
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return "Attribute must be a string type!"

    def __check_attribute(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be a {should_be} type!")

user_card_1 = Card("2344 2345 4354 7564", 123.0)
print(user_card_1.get_card_data())

