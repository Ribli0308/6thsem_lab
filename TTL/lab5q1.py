'''1. wap to check if 2 given sets have common element or not.'''
myset1 = (1, 2, 3, 4, 5)
myset2 = (7, 6, 8, 3, 9)
print(myset1)
print(myset2)
print("Is there any common element between the two sets")
isPresent = False
for elem in myset1:
    if elem in myset2:
        isPresent = True
print(isPresent)
    