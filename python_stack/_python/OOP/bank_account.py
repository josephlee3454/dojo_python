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
        print(f'your actual balance is {self.balance}')


acct1 = Bank(name="jim",balance=25)
acct1.withdraw(100).deposit(125).account_ballance()