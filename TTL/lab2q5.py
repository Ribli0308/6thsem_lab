def reverseNumber(number):
    reverse = 0
    while number > 0:
        num = number % 10
        reverse = (reverse * 10) + num
        number = number // 10
    return reverse

num = int(input("Enter a number: "))
print("The reversed number is ", reverseNumber(num)) 