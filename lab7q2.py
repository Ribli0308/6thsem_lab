#2. wap class named student with two instances student 1 and student2 declare suitable data members or member functions to display their values.
class Student:
    def __init__(self, name, rollno, m1, m2, m3):
        self.name = name
        self.roll = rollno
        self.m1, self.m2, self.m3 = m1, m2, m3
    def percentage(self):
        total = self.m1 + self.m2 + self.m3
        percentage = (total / 300) * 100
        return percentage
    def details(self):
        print('Name: ', self.name)
        print('RollNumber: ', self.roll)
student1 = Student('Mars', 879, 89, 76, 94)
print('percentage: ',student1.percentage())
student1.details()
student2 = Student('Venus', 898, 67, 76, 88)
print('percentage: ',student2.percentage())
student2.details()