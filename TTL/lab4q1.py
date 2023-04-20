''' WAP to get the second smallest and second largest elem present in a list.'''
lst = [3, 4, 7, 8, 11, 33, 27, 1]
print(lst)
for i in range(len(lst)-1):  
    for j in range(len(lst)-1):  
        if(lst[j]>lst[j+1]):  
            lst[j], lst[j + 1] = lst[j + 1], lst[j] 
print(lst)
print("Second smallest element: ", lst[1])
print("Second largest element: ", lst[-2])