def checkPerfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

y = int(input("Enter a number"))
print("Is the given number perfect? ", checkPerfect(y))