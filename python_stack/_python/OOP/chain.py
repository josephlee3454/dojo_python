class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.trans_num = 4000
       
    
    def deposit(self,amount):
        self.balance += amount
        self.trans_num += 1
        print(f'Balance {self.balance}, Amount {amount}, transaction # {self.trans_num}, Customers Name: {self.name}')
        return self
    
    def withdraw(self,amount):
        self.balance -= amount
        self.trans_num += 1
        print(f'Balance {self.balance}, Amount {amount}, transaction # {self.trans_num}, Customers Name: {self.name}')
        return self 
        
    def transfer(self,amt,users):

        print("**********transfers***************")
        x = self.withdraw(amt)
        users.deposit(amt)
        # print(users.deposit(amt))
        return self





user1 = User(name="jim",balance=25)
user2 = User(name="fred", balance=200)
user3 = User(name="molly", balance=3000)


user1.deposit(100).deposit(100).deposit(300).withdraw(300)

user2.deposit(100).deposit(100).withdraw(1000).withdraw(50)

user3.deposit(1000).withdraw(1000).withdraw(1000).withdraw(50)



# Bonus the transfer 

user2.transfer(100,user1)

