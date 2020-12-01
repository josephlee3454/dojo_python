# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
# [x] Create a file with the User class, including the __init__ and make_deposit methods
# [x] Add a make_withdrawal method to the User class
# [x] Add a display_user_balance method to the User class
# [x] Create 3 instances of the User class
# [x] Have the first user make 3 deposits and 1 withdrawal and then display their balance
# [x] Have the second user make 2 deposits and 2 withdrawals and then display their balance
# [x] Have the third user make 1 deposits and 3 withdrawals and then display their balance
# [x] BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.trans_num = 4000
    
    def deposit(self,amount):
        self.balance += amount
        self.trans_num += 1
        print(f'Balance {self.balance}, Amount {amount}, transaction # {self.trans_num}, Customers Name: {self.name}')
    
    def withdraw(self,amount):
        self.balance -= amount
        self.trans_num += 1
        print(f'Balance {self.balance}, Amount {amount}, transaction # {self.trans_num}, Customers Name: {self.name}')
    
        
    def transfer(self,amt,users):

        print("**********transfers***************")
        x = self.withdraw(amt)
        users.deposit(amt)
        # print(users.deposit(amt))





user1 = User(name='lenny', balance=600)
user2 = User(name="fred", balance=200)
user3 = User(name="molly", balance=3000)


user1.deposit(100)
user1.deposit(100)
user1.deposit(300)
user1.withdraw(300)

user2.deposit(100)
user2.deposit(100)
user2.withdraw(1000)
user2.withdraw(50)

user3.deposit(1000)
user3.withdraw(1000)
user3.withdraw(1000)
user3.withdraw(50)



# Bonus the transfer 

user2.transfer(100,user1)


