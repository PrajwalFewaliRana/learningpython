class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accountNum = acc
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"is debited from your account Number:",self.accountNum)
        print("Remaining balance is:",self.showBal())
        
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"is credited to your account Number:",self.accountNum)
        print("Remaining balance is:",self.showBal())
        
    def showBal(self):
        return self.balance

a1 = Account(120000,12349138530012)
a1.debit(12000)
a1.credit(50000)