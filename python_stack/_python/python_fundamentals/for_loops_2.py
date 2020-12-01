# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(arr):

#     for i in range(len(arr)):
#         if arr[i] > 0:
#            arr[i] = "biggie"
#     print(arr)
#     return arr

# arr = [-1,3,5,-5]
# biggie_size(arr)

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the 
# number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def count_positive(arr):
#     num = 0
#     for i in range(len(arr)-1):
#         if arr[i] > 0:
#             num = num + 1
#             x = len(arr)-1
#             arr[x] = num 
#     print(arr)
# arr = [1,6,-4,-2,-7,-2]
# count_positive(arr)

# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# def sum_total(arr):
#     sum = 0 
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     print(sum)
#     return sum 
# arr = [1,2,3,4]
# sum_total(arr)
        
# 4) Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
# def average_x(arr):
#     divder = 0
#     sum_num = 0 
#     for i in range(len(arr)):
#         sum_num = sum_num + arr[i]
#         divder = divder + 1
#         average = sum_num / divder
#     print(average)
#     return average
# arr = [1,2,3,4]
# average_x(arr)  

# 5) Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# # Example: length([]) should return 0
# def return_length(arr):
#     length = 0 
#     for i in arr:
#         length = length + 1
#     print(length)
#     return length

# arr = [37,2,1,-9]
# return_length(arr)

# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(arr):
#     if arr:
#         min_val = arr[0]
#         for i in range(len(arr)):
#             if arr[i] < min_val:
#                 min_val = arr[i]
#         print(min_val)
#         return min_val
#     else:
#         return False
# arr = [37,2,1,-9]
# minimum(arr)

# 7) Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the
#  function return False.
# Example: maximum([37,2,1,-9]) should return 37
# # Example: maximum([]) should return False
# def max(arr):
#     if arr:
#         max_val = arr[0]
#         for i in range(len(arr)):
#             if arr[i] > max_val:
#                 max_val = arr[i]
#         print(max_val)
#         return max_val
#     else:
#         print(False)
#         return False
# arr = [37,2,1,-9]
# max(arr)




#8)  Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list. Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
analysis = {}
def ultimate_analysis(arr):
    min_val = arr[0]
    max_val = arr[0]
    sum_total = 0 
    for i in range(len(arr)):
        sum_total = sum_total + arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    lengthed = len(arr)
    average = sum_total/lengthed 
    analysis['sumTotal'] = sum_total 
    analysis['average'] = average 
    analysis['minimum'] = min_val 
    analysis['maximum'] = max_val
    analysis['length'] = lengthed
    print(analysis)
    return analysis
arr = [37,2,1,-9]
ultimate_analysis(arr)






# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]



# def reverse_list(arr):
#     x = len(arr)-1
#     for i in range(len(arr)//2):
#         temp = arr[i]
#         arr[i] = arr[x]
#         arr[x] = temp
#         x = x + -1
#     print(arr)
#     return arr
# arr = [37,2,1,-9]
# reverse_list(arr)

