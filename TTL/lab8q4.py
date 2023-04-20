class Employee:
    def empDetails(self, id, age, name):
        self.id = id
        self.age = age
        self.name = name

class RegularEmp(Employee):
    def salary(self, Basic):
        self.basic = Basic
        self.DA = 0.05 * self.basic 
        self.TA = 0.1 * self.basic
        self.gross = self.basic + self.DA + self.TA
        print(self.id, self.age, self.name)
        print(self.gross)

class DailyWorker(Employee):
    def workDetails(self, days, wagesPerDay, OT):
        self.days = days
        self.wagesPerDay = wagesPerDay
        self.OT = OT
        self.salary = (self.days + self.OT) * self.wagesPerDay
        print(self.id, self.age, self.name)
        print(self.salary)

obj1 = RegularEmp()
obj1.empDetails(1201, 34, 'Atul')
obj1.salary(5678)
obj2 = DailyWorker()
obj2.empDetails(3456, 28, 'Vinay')
obj2.workDetails(23, 3000, 5) 