def calculate(m1, m2, m3, m4):
    total = m1 + m2 + m3 + m4
    percentage = (total / 400) * 100
    print("Percentage is ", percentage)
    print("Grade is: ",displayGrade(percentage))

def displayGrade(percentage):
    number = int(percentage // 10) 
    match number:
        case 10:
            return 'O'
        case 9:
            return 'O'
        case 8:
            return 'E'
        case 7:
            return 'A'
        case 6:
            return 'B'
        case 5:
            return 'C'
        case 4:
            return 'D'
        case default:
            return 'F'

m1 = int(input("Enter marks of sub1"))
m2 = int(input("Enter marks of sub2"))
m3 = int(input("Enter marks of sub3"))
m4 = int(input("Enter marks of sub4"))

calculate(m1, m2, m3, m4)
