'''4. wap that finds all pairs of elements in a list whose sum is equal to a given value.'''
list1 = [2, 4, 5, 6, 11, 33, 56, 3, 3]
val = int(input("Enter sum"))
myset1 = set()
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == val:
            myset1.add((list1[i], list1[j]))
print(myset1)
