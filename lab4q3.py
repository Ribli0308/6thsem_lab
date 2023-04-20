'''wap to find out the index of an elem in a specified list.'''
list1 = []
n = int(input("specify elements"))
for i in range(0, n):
    k = int(input("enter element"))
    list1.append(k)
elem = int(input("enter the element whose index needs to be found: "))
count = 0
for elm in list1:
    if elm == elem:
        print('index ', count)
        break
    count += 1
    