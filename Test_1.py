Name = 5
you = 54
print(Name + you)

name = "Youu"
nAme = 'Youu'
print("First try: " + name)
print(f"{type(name)} + {type(nAme)}")

if name == "You": print("Yes")
else: print("Second try: No")

result = Name < you and Name == 5
print(f"Third try: {result} and your age ({Name})")

print(f"Check type Name: {type(Name)}")

print(len(str(result)))

string = ('Wassaaaaap')
string_list = list(string)

unique_list = list(dict.fromkeys(string_list))
print(unique_list)