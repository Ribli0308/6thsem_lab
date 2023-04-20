'''4. wap to generate a multiplication table of any number using lambda function.'''
def multiplication(a):
    for i in range(1, 6):
        prod = lambda a: a * i
        print(a ,' * ', i, ' = ', prod(a))

multiplication(3)