'''3. wap to check an entered value is present in the set or not.'''
n = int(input("Specify size"))
myset = set()
for i in range(n):
    myset.add(int(input("enetr element")))
print(myset)
k = int(input("enetr a value"))
print("Is the value present in set? ", k in myset)