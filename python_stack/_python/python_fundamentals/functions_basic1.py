#1 



def a():# function a
    return 5# return 5 when function called 
print(a()) # print return value of function which is 5 

#                    var | val
#                    __________
#                  return|  5
#             prnt(a())  | print the return value of function a 
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |


# #2


def a(): # define function a 
    return 5 # return 5 when function is called
print(a()+a()) # print the return result for both function a's  and add them together 

#                    var | val
#                    __________
#         return 5       | 5
#      print a() + a()   | 5 + 5 = 10
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |






#3
def a(): # define function a
    return 5 # return 5 after function called
    return 10
print(a())# print the result of the function after its called wich will print the first return statement 5 
#                    var | val
#                    __________
#          1st  return 5 |  5
#      second return 10  |  10 wont print 10 as it is will only print 5 since its first return 
#          print(a())    |  5
#                        |  
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |



# #4
def a():# define function a 
    return 5  # return 5 after function call 
    print(10) # wont print 10 since it is afte the return statement 
print(a()) #print the return statement which is 5 


#                    var | val
#                    __________
#              return  5 | 5
#              print(10) |  10
#            print(a())  | 5 
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |





# #5
def a(): # define function a 
    print(5) # print 5
x = a()  # assign the function a to x 
print(x) # print the result of function  


#                    var | val
#                    __________
#                print   | 5 
#                x       | a() => 5
#                print x | None
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |



# #6
def a(b,c):# define function a pass in b and c 
    print(b+c) # print the sume of b and c 
print(a(1,2) + a(2,3)) # error


#                    var | val
#                    __________       func1  func2 
#              print     | b + c   ||  1+2 || 2+3 
#                        |   3
#                        |   5
#                 print  |   error
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |






# #7
# def a(b,c): # define function a and pass in a and b 
#     return str(b)+str(c) # return the addittion  b and c but first stringify them 
# print(a(2,5)) # print the function a pass in 2 and 5 
# but when you add them you are adding strings so it wont add like 
# numbers it will put the two strings next to each other.

#                    var | val
#                    __________
# return str(b) + str(c) | "ab"
#       print(a(2,5))    | "25"
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |
#                        |





# #8
def a(): # define function a 
    b = 100 # assign 100 to b 
    print(b) # print 100
    if b < 10: # if b is less than 10 
        return 5 # if condition above is met then return 5
    else:# anything else then the condition above 
        return 10 # return 10 if anything other than b being less than 10
    return 7# return statement to return 7 but wont happen becuase the return statemnet above overwrites it 
print(a()) # print the print statement sice above the return statement and after that print the else condition which is 10 


#                    var | val
#                    __________
#                     b  | 100
#                print(b)| 100
#                1st if  | return 5 if condition is met 
#                2nd if  |  return 10 if condition is met 
#               return 7 |  wont return 7
#              print(a)  |  print b and print the return statement 
#                        |
#                        |
#                        |
#                        |





#9
def a(b,c): # define function a and pass in b and c 
    if b<c: # if b is less thean c
        return 7 # return 7 if the condition is met above 
    else:#elses anything else 
        return 14 # anything else return 14
    return 3 # return 3 wont happen 
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#                    var | val
#                    __________
#               if       | if b is less than c
#               return   |   7 
#                else    | else anything else 
#                return  | if else than 14
#               return   | 3 but wont happen 
#          print(a(2,3)) |  7
#          print(a(5,3)) |  14
# print(a(2,3) + a(5,3)) | 21
#                        |
#                        |



# # #10
def a(b,c):  # define function a and pass in b and c 
    return b+c # return the sum of b and c 
    return 10 # return 10 but wont happen becuase the first return stement overides the second 
print(a(3,5)) # print 8

# #                    var | val
# #                    __________
# #              return    | b + c =  8 
# #               return   | 10
# #        print(a(3,5))   | 8
# #                        |
# #                        |
# #                        |
# #                        |
# #                        |
# #                        |
# #                        |


#11
b = 500 # assign b to 500
print(b) # print b which is 500
def a(): # define function a 
    b = 300 # reassign b to 300
    print(b)# print 300
print(b) # print 500 becuase it is not in the function 
a()# call function a which will print 300
print(b) # print 500 

#                    var | val
#                    __________
#                 b      | 500
#              print(b)  |  500 
#      b  insde function | 300
#print(b)outside function|  500
#               a()      |  print(b) = 300
#           print(b)     | 500
#                        |
#                        |
#                        |
#                        |


#12
b = 500 # assign b to 500 
print(b) # print b whihc is 500 
def a(): # define function a
    b = 300 # assign b to 300 
    print(b) # print 300
    return b # return b which is 300 
print(b) # print 500 becuase thats what b is outside the function 
a() # call function a 
print(b) # print b  which is 500 because it is also out side the function 

#                    var | val
#                    __________
#                     b  | 500
#              print(b)  | 500 
#          b insde func  | 300
#            print(b)    | 300 becuase its in the function 
#             return     |  300
#            print(b)    | 500
#             a()        | print and return 300 
#           print(b)     | 500
#                        |
#                        |


# #13
b = 500 # assign b to 500
print(b) # print 500
def a(): #define function a 
    b = 300 # assign b to 300
    print(b) # print 300
    return b # return 300
print(b) # print 500
b=a() #assign b to function a 
print(b)# print result of function becuase you reassigned b 

#                    var | val
#                    __________
#                  b     | 500
#                  print | 500
#                    b   | 300   ---
#                print(b)| 300      | inside function its 300
#                return b| 300   ---
#               print(b) | 500
#               b=a()    | print and return 300
#              print(b)  | 500
#                        |
#                        |






# #14
def a(): # define function a 
    print(1) # print 1 
    b() # call function b 
    print(2) # print 2 
def b(): # define function b
    print(3)# print 3
a()# call function a 


#                    var | val
#                    __________
#      1st func print    | 1
#                b()     | 3
#               print    | 2
#                        |
#     2nd function print |  3
#                        |
#                        |
#            a()         |   1,3,2
#                        |
#                        |





#15
def a(): # define function a 
    print(1) # print 1 
    x = b() # assifn x to function a 
    print(x) # print the rsult of funtion a 
    return 10 #return 10 
def b(): # define function b 
    print(3) # print 3 
    return 5 # return 5
y = a()  # assing y to function a 
print(y) # print the result of function y 



#                    var | val
#                    __________
#                  print | 1
#                    x   | b()
#                print(x)| 3,5
#              return 10 | 10
#       second function  |
#          print         | 3
#              return    | 5
#               y        | a()
#              print(y)  | 1,3,5,10
#                        |
