def fibonacciSeries(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, b + a
        print(a)

y = int(input('Enter number of terms: '))        
fibonacciSeries(y)