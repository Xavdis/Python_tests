class Person:
    name = "Empty"
    age = "Empty"


print(Person.name)
print(Person.age)
per = Person()
per.name = "Tom"
print(per.name)
print(per)
per2 = Person()
per2.name = "Tom2"
print(per.name)
per2.age = 30
print(f"{per.age} + {per2.age}")
print(per2.__dict__)


setattr(per2, "name", "Duck")
print(getattr(per2, "name"))

