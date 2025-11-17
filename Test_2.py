import pandas as pd

test_list = ["Hello", "daddy", "your"]

if test_list == ["Hello", "daddy"]:
    print("No, this list is`t right")
elif test_list == ["Hello", "daddy", "your"]:
    print("Yes this list is right")

a = 10
b = 15
c = 45

if a>b:
    print("Take your time")
elif a<b:
    print("Don`t push the hourses")
else:
    print("i think your data wrong")

userData = {
    "Name": ["Daddy", "Tom", "Gay"],
    "Age": [10, 20, 30],
    "balance": [500, 650, 150]
}
df = pd.DataFrame(userData)
print(df)

if "Daddy" in userData["Name"]:
    print(userData["Name"].index("Daddy"))
    print(userData.get("Name"))
    print(userData.get("Age"))
    print(userData.get("balance"))
    print(f"This is: {userData['Name'][0]} and he is:")
