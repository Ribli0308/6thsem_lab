def calculate(m1, m2, m3, m4):
    total = m1 + m2 + m3 + m4
    percentage = (total / 400) * 100
    print("Percentage is ", percentage)
    print("Grade is: ",displayGrade(percentage))

def displayGrade(percentage):
    if percentage >= 90:
        return 'O'
    if percentage >= 80:
        return 'E'
    if percentage >= 70:
        return 'A'
    if percentage >= 60:
        return 'B'
    if percentage >= 50:
        return 'C'
    if percentage >= 40:
        return 'D'
    return 'F'

m1 = int(input("Enter marks of sub1"))
m2 = int(input("Enter marks of sub2"))
m3 = int(input("Enter marks of sub3"))
m4 = int(input("Enter marks of sub4"))

calculate(m1, m2, m3, m4)
