class Bank:
    def __init__(self, balance, name):
        self.balance = balance 
        self.rate = 0.1
        self.name = name 
    
    def withdraw(self,amount):# withdraw method 
        self.balance -= amount
        print(f'amount to be withdrawn {amount} amount after withdraw {self.balance} ')
        return self

    def deposit(self,amount):#deposit method 
        self.balance += amount
        print(f'amount to be deposited {amount} after deposit {self.balance}')
        return self
    
    def account_ballance(self):
        print(f'{self.name} your actual balance is {self.balance}')
    
    def yield_interest(self):
        self.balance * self.rate
        print(f'{self.name} your interest return is {self.balance * self.rate}')
        return self 


acct1 = Bank(name="jim",balance=25)
acct2 = Bank(name="pam",balance=2500)
acct1.withdraw(100).deposit(125).deposit(325).deposit(1000).yield_interest().account_ballance()

acct2.withdraw(100).withdraw(100).withdraw(100).withdraw(100).deposit(125).deposit(125).yield_interest().account_ballance()