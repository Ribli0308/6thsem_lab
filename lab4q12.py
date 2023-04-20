'''wap to create a tuple with nested tuple and list and access and print the elem of nested tiple and list.'''
list1=[]
n=int(input("Enter number of elements:"))

for i in range(0,n):
    k=int(input("Enter the number:"))
    list1.append(k)
  
print("Printing tuple with above list nested:")
tup1=('hello', 5 , 6, 7, list1)
print(tup1)

print("\nPrinting the list nested inside tuple: ", tup1[4] )
'''a = ()

n = int(input("enter the numebr of elements : "))

for i in range(n):

    k = int(input("enter 1 for num 2 for list : "))
    if k == 1:
        k = int(input("enter num : "))
        a = list(a)
        a.append(k)
        a = tuple(a)
    else:
        b = []
        n = int(input("enter the number of elements : "))
        for i in range(n):
            k = int(input("enter num : "))
            b.append(k)
        a = list(a)
        a.append(b)
        a = tuple(a)

print(a)
for i in a:
    if (type(i) is list):
        print(i)'''