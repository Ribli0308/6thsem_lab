def checkArmstrong(num):
    total, dup = 0, num
    while num > 0:
        digit = num % 10
        total += digit ** 3
        num = num // 10
    return total == dup

y = int(input("Enter a three digit number: "))
print("IS the given number an armstrong number? ", checkArmstrong(y))
