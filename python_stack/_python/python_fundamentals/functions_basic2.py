# 1) Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
        print(arr)
    return arr
num = 5
countdown(num)

# 2) Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_return(num1,num2):
    print(num1)
    return num2
num1 = 1
num2 = 2
# print(print_return(num1,num2)))
print_return(num1,num2



# 3) First Plus Length - Create a function that accepts a list and returns the sum of the 
# first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(arr):
    x = arr[0] + len(arr)
    return x 
arr = [1,2,3,4,5]
first_plus_length(arr)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the
#  values from the original list that are greater than its 2nd value. Print how many values this is and then return 
# the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def greater_second(arr):
    new_arr = []
    for i in arr:
        if i > arr[1]:
            new_arr.append(i)
    print(len(new_arr))
    return new_arr

arr = [5,2,3,2,1,4]
greater_second(arr)
print(greater_second(arr))


# This Length, That Value - Write a function that accepts two integers 
# as parameters: size and value. The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_that_value(arr_size, arr_value):
    arr = []
    for i in range(arr_size):
        arr.append(arr_value)
    print(arr)
    return arr
arr_size = 4
arr_value = 7
length_that_value(arr_size, arr_value)