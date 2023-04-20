def findMin(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return a
    elif b > c and b > d and b > e:
        return b
    elif c > d and c > e:
        return c
    elif d > e:
        return d
    return e

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
d = input("Enter d: ")
e = input("Enter e: ")
print("the max value is: ", findMin(a, b, c, d, e))
