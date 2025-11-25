import def_for_test
import turtle

def add_int(a,b):
    newList = []
    newList.append(a)
    newList.append(b)
    c1 = a+b
    newList.append(c1)
    return a+b

def hello(string):
    print(f"Hello World, {string}")


a = 4
b = 2
print(add_int(a,b))
hello("Dyadya")
def_for_test.helloo("Dyadya")


def kwardat():
    i = 0
    while i<3:
        turtle.forward(150)
        turtle.left(90)
        i += 1

def kwadratFor(size, color):
    turtle.speed(5)
    turtle.color(color)
    def move():
        turtle.forward(size)
        turtle.left(90)
    for _ in range(4):
        move()

for _ in range(6):
    kwadratFor(150, 'red')
    turtle.color('black')
    kwadratFor(250, 'blue')
    turtle.left(90)
