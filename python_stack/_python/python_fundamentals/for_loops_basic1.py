# Assignment: For Loops: Basic I
# Objectives:
# Learn how to use basic for loop statements in Python
# Practice some basic algorithms in Python

# Create a Python file called for_loop_basic1.py that performs the following tasks.


1) Basic - Print all integers from 0 to 150.
def all_print():
    for i in range(151):
        print(i)
all_print()


# 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def mutiples_five():
    for i in range(151):
        if i % 5 == 0:
            print(i)
mutiples_five()

# 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print 
"Coding Dojo".
def dojo_way():
    for i in range(100):
        
        if i % 10 == 0:
            print("Coding Dojo")
        if i % 5 == 0:
            print("Coding")
        else:
            print(i)
# dojo_way()        

# 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def huge_sucker():
    num = 0
    for i in range(500000):
        num += i
        print(num)
huge_sucker()

# 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.



def countdown_fours():
    for i in range(2018, 0, -4):
        print(i)
countdown_fours()




# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop 
# should print 3, 6, 9 (on successive lines)

def countdown_fours():
    for i in range(2 , 10):
        if i % 3==0:
            print(i)
countdown_fours()


