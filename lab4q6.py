'''wap to remove the kth elem and print the updated list.'''
list1 = []
n = int(input("specify elements"))
for i in range(0, n):
    k = int(input("enter element"))
    list1.append(k)
print(list1)
k = int(input("enter the value of k"))
list1.remove(list1[k])
print(list1)