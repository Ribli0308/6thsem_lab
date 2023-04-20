'''wap to print a specified list after removing second and fifth index elem.'''
list1 = []
n = int(input("specify elements"))
for i in range(0, n):
    k = int(input("enter element"))
    list1.append(k)
print(list1)
elem2 = list1[2]
elem5 = list1[5]
list1.remove(elem2)
list1.remove(elem5)
print(list1)