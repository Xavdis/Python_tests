from types import new_class

from fontTools.misc.cython import returns


class Car:
    marka = []
    color = []
    engine = []

def add_car():
    Car.marka.append(input(f"Please write Marka: "))
    Car.color.append(input(f"Please write Color: "))
    Car.engine.append(input(f"Please write Engine: "))

def check_writen_symb(yon, i):
    if i == 2:
        while yon not in ['y', 'n']:
            yon = input('Try again [y/n]: ')
    elif i == 3:
        while yon not in ['y', 'n', 'a']:
            yon = input('Try again [y/n/a]: ')
    return yon

def show_all_cars():
    print(f"Marka: {Car.marka}\nColor: {Car.color}\nEngine: {Car.engine}")

yesOrNo = input("Hello, do you want add same car to our data base? "
                "Just write 'a' to see all data base. "
                "Press 'n' to exit. [y/n/a]: ")

yesOrNo = check_writen_symb(yesOrNo, 3)
while yesOrNo in ['y', 'a']:

    if yesOrNo == 'y':
        print(f"We have three options: Marka, Color, Engine")
        while yesOrNo == 'y':
            add_car()
            yesOrNo = check_writen_symb(input("You want add another car to our data base? "
                                              "Press 'a' to see all cars. Press 'n' to exit. [y/n/a]"), 3)


    elif yesOrNo == 'a':
        show_all_cars()
        yesOrNo = check_writen_symb(input("You want add car to our data base? To show"
                                          "all cars press 'a'. Press 'n' to exit. [y/n/a]: "), 3)

if yesOrNo == 'n':
    exit("Goodbye. You exit from program.")