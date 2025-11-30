class UserData():
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password_input):
        if password_input == self.__password:
            return "Password is right!"
        else:
            return "Password is wrong!"