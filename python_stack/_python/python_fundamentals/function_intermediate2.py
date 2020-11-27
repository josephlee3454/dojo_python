# # 1) Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
# def change_val():
#     x[1][0] = 15
#     students[0]['last_name'] = 'Bryant'
#     sports_directory['soccer'][0] = 'Andres'
#     z[0]['y'] = 30
#     print(sports_directory)
#     print(students)
#     print(z)
#     print(x)
#     return x
# change_val()




# 2)Iterate Through a List of Dictionaries



# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(students):
#     num = 0 
#     for i in students: 
#         dicter = i
#         # print(i)
#         for key, value in dicter.items():
#             print(key + " -",value+",")
            
    
       
#     return students
# iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel






# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# 3) Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel
# def iterateDictionary(key_val,students):
#     num = 0 
#     for i in students:
#         print(students[num][key_val])
#         num = num +1
    
       
#     return students
# key_val = 'first_name' # this is for the first name 
# # key_val = 'last_name' # this is for the last name 
# iterateDictionary(key_val,students)



#4)  Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def iterate_list_vals(dojo):
    for key,value in dojo.items():
        print(len(value) , key)
        for i in value:
            print(i)
iterate_list_vals(dojo)



# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon