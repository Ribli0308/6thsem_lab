'''wap to change the pos of every nth element with n + 1 element in the list.'''
list1 = []
n = int(input("specify elements"))
for i in range(0, n):
    k = int(input("enter element"))
    list1.append(k)
print(list1)
for i in range(0, len(list1), 2):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]
print(list1)