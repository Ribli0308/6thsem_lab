class Student:
    def details(self, name, grade, roll):
        self.name = name
        self.grade = grade
        self.roll = roll

class Exam(Student):
    def score(self, mark1, mark2, mark3):
        self.average = (mark1 + mark2 + mark3) * 3
        self.percentage = self.average * 100

class Activities:
    def cocurricularActivities(self, act1, grade1, act2, grade2):
        print("activity1: ", act1)
        print("grade1: ", grade1)
        print("activity2: ", act2)
        print("grade2: ", grade2)

class Result(Exam, Activities):
    pass
