# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be[[5, 2, 3], [15, 8, 9]].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# 1. (x[1][0]) = 15
# print(x)

# # 2. students [0] ["last_name"] = "Bryant"
# # print(students)

# 3. sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

# 4. z[0]['y'] = 30
# print(z)

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines
#                 bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 2. for index in range(len(students)):
#     for key in students[index]:
#         print(students[index][key])

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# 3. def iterateDictionary2(key, listname):
#     for listitem in listname:
#         print(listitem[key])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(some_dict):
#     for key in some_dict:
#         print(f"{len(some_dict[key])} {key} ")
#         for x in some_dict[key]:
#             print(x)


# printInfo(dojo)
# output:
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
