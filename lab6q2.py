'''2. wap to pass a list to a func, now func adds 3 to each and every element to the list and then prints the updated list in the func calling part.'''
def myFunc(lst):
    for i in range(len(lst)):
        lst[i] += 3
    print(lst)
myFunc([1, 2, 3, 4, 5, 6, 7, 8])