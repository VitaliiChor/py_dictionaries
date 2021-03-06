"""
1. Sum Values
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary
"""
# Write your sum_values function here:
# ======================================
# def sum_values(my_dictionary):
#   sum = 0
#   for value in my_dictionary.values():
#     sum += value
#   return sum

# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# ========================================
# Uncomment these function calls to test your sum_values function:
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


"""
2. EvenKeys
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
as a parameter. This function should return the sum of the values of all even keys.
"""


# Write your sum_even_keys function here:
# =========================================
# def sum_even_keys(my_dictionary):
#   sum = 0
#   for num in my_dictionary.keys():
#     if num % 2 == 0:
#       sum += my_dictionary[num]
#   return sum

# print(sum_even_keys({1:5, 2:2, 3:3}))
# ===========================================
# Uncomment these function calls to test your  function:
# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
# print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


"""
3. Add Ten
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary
"""
# Write your add_ten function here:
# ===================================
# def add_ten(my_dictionary):
#   for num in my_dictionary.keys():
#     my_dictionary[num] += 10
#   return my_dictionary

# print(add_ten({1:5, 2:2, 3:3}))
# =====================================
# Uncomment these function calls to test your  function:
# print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


"""
4. Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
"""
# Write your values_that_are_keys function here:
# =============================================
# def values_that_are_keys(my_dictionary):
#   keys = []
#   for key in my_dictionary.values():
#     if key in my_dictionary.keys():
#       keys.append(key)
#   return keys

# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# ===============================================
# Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


"""
5. Largest 
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary.
"""
# Write your max_key function here:

# Uncomment these function calls to test your  function:
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
