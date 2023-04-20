'''3. wap to pass a number to a func, then print 1, 2, 3, 4 ..n using recursion.'''
def series(n, i = 1):
    if i > n:
        return 0
    print(i, end = " ")
    series(n, i + 1)

series(8)
