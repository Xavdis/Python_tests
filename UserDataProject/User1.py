import UserData as ud

user1 = ud.UserData("Ted", "FFFF")
password1 = input("Enter Password: ")
while user1.check_password(password1) == "Password is wrong!":
    print(user1.check_password(password1))
    password1 = input("Enter Password: ")
else:
    print("Password is right! Welcome!")