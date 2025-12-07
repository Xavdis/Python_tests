def CheckName(name_list):
    for name in name_list:
        if name[0] == 'A':
            yield name

names = ["Alex", "Bob", "Anna", "John", "Alice"]

nameA = CheckName(names)
for name in nameA:
    print(name)