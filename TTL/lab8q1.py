class Bank_acc:
    
    def info(self,acc_num, balance, cust_name):
        self.acc_num=acc_num
        self.balance=balance
        self.cust_name=cust_name
        
        
class Customer(Bank_acc):
    def display(self):
        print("Name: ", self.cust_name)
        print("Account Number: ", self.acc_num)
        print("Current balance: ", self.balance)

obj1 = Customer()
obj1.info(23456, 10000, 'Ally')
obj1.display()

obj2 = Customer()
obj2.info(13657, 15000, 'Austin')
obj2.display()