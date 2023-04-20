#5. wap class to implement pow[x,n].
class Number:
    def pow(self, x, n):
        if n<0:
            power = 1
            for i in range(-1 * n):
                power *= x
            return 1/power
        
        power = 1
        for i in range(n):
            power *= x
        return power

power = Number()
print(power.pow(3, 4))
print(power.pow(3, -1))
print(power.pow(3, 9))