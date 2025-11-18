from traceback import clear_frames

import pandas as pd

newList = {
    "Tag": ["GG", "WP", "GL"],
    "Meaning": ["Good Game", "Well played", "Good luck"],
    "Id": []
}

for word in newList["Tag"]:
    print("=========================")
    ind = newList["Tag"].index(word)
    print(word)
    print(newList["Meaning"][ind])

print("=========================")

a = 1
while a <= 3:
    print(a)
    newList["Id"].append(a)
    a += 1
    print(newList["Id"])

NewList = pd.DataFrame(newList)
print(NewList)

A = [1, 2, 3, 5, 2, 6, 4, 8, 9]
A = A[::-1]
B = [3,2,4,3,5,5,6,3,2,4,1,2,4,3]

count = B.count(3) - 1
print(count)
while count > 0:
    B.remove(3)
    print(B)
    count -= 1

print("\a",A)
print(B[:7])
print(B)
A.sort()
print(A)