#8. wap class called bank account with attributes: acc no, balance, cust name and methods: deposit, withdraw and check balance and print the values.
class bank_acc:
    
    def info(self,acc_num, balance, cust_name):
        self.acc_num=acc_num
        self.balance=balance
        self.cust_name=cust_name
        
    def deposit(self,new_amt):
        self.new_amt=new_amt
        print("Current balance:", self.balance)
        self.balance=self.balance+self.new_amt
        print("Balance after depositing:", self.balance)
        
    def withdraw(self,taken):
        self.taken=taken    
        self.balance=self.balance-self.taken
        print("Balance after withdrawing money:", self.balance)
        
    def check_balance(self):
        print("Final Balance:", self.balance)
        
        
new_bankacc=bank_acc()
new_bankacc.info(2344, 10000, "Devashree")
new_bankacc.deposit(3500)
new_bankacc.withdraw(700)
new_bankacc.check_balance()