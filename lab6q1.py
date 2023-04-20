'''1. wap to calculate simple interest of the given ptr using function where the function takes the default value for r.'''
def simpleInterest(p, t, r = 2):
    a = (p * t * r) / 100
    return a + p

print(simpleInterest(12000, 3, 5))