class University:
    def uniDetails(self, uniName, degree, year, joinYear):
        self.uniName = uniName
        self.degree = degree
        self.year = year
        self.joinYear = joinYear

class School:
    def schoolDetails(self, schoolName, board, yearOfPass, percentage):
        self.schoolName = schoolName
        self.board = board
        self.yearOfPass = yearOfPass
        self.percentage = percentage

class Student(University, School):
    def printDetails(self):
        print('uniName: ', self.uniName)
        print('degree: ', self.degree)
        print('year: ', self.year)
        print('joinYear: ', self.joinYear)
        print('schoolName: ', self.schoolName)
        print('board: ', self.board)
        print('yearOfPass: ', self.yearOfPass)
        print('percentage', self.percentage)

student1 = Student()
student1.uniDetails('KIIT', 'CSE Btech', 3, 2020)
student1.schoolDetails('DPS', 'CBSE', 2020, '93.2')
student1.printDetails()