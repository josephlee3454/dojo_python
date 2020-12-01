class Bank:
    def __init__(self, balance, name, rate):
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

class User:
    def __init__(self,name,balance):
        self.name = name
        self.account = Bank(balance=100,name='name',rate=.01)
        self.trans_num = 4000
    
    def dep(self,amount):
        self.account.deposit(100)
        
    
    def withd(self,amount):
        self.account.withdraw(200)
    
    def disp(self):
        self.account.account_ballance()
        
    def transfer(self,amt,users):

        print("**********transfers***************")
        x = self.withdraw(amt)
        users.dep(amt)
        # print(users.deposit(amt))





user1 = User(name='lenny', balance=600)
user2 = User(name="fred", balance=200)
user3 = User(name="molly", balance=3000)


user1.dep(100)
user2.withd(225)
user3.disp()