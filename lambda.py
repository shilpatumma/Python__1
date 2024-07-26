# addition  :

# add = lambda num : num + 4
# print(add(4))



# def and lambda keyword :

# def reciprocal(num):
#     return 1/num

# lambda_reciprocal = lambda num:1/num
# print(reciprocal(2))
# print(lambda_reciprocal(2))



# Practice Question : 
# (a). Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result.

# Ans...

# add = lambda num : num + 15
# print(add(15))

# mul = lambda x,y : x * y 
# print(mul(21,2))



# (1).Create a lambda function to add two numbers.
# Create a lambda function to multiply two numbers.
# Create a lambda function to calculate the square of a number.
# 

# Ans...

# addition  = lambda x,y : x + y
# print(addition(10,20))

# multiplication = lambda x,y : x * y
# print(multiplication(10,20))

# square  = lambda x : x**2
# print(square(10))



# (2). Create a lambda function to concatenate two strings.
# Create a lambda function to get the first character of a string.
# Create a lambda function to convert a string to uppercase.

# Ans...

# concat_two_strings = lambda s1, s2: s1 + s2
# result = concat_two_strings("Good ", "Morning")
# print(result)


# get_first_char_of_string = lambda c : c[0]
# result = get_first_char_of_string("Python")
# print(result)


# uppercase = lambda s: s.upper()
# result = uppercase("python, java, jquery")
# print(result)






# (3). Sort a list of tuples based on the second element.
# Sort a list of dictionaries based on a specific key.
# Sort a list of strings based on their length

# Ans...

# tuples_list = [(1, 3), (3, 2), (2, 1)]
# sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
# print(sorted_tuples)  # Output: [(2, 1), (3, 2), (1, 3)]



# dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
# sorted_dicts = sorted(dict_list, key=lambda x: x['age'])
# print(sorted_dicts)  # Output: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]



# list_of_strings = ["apple", "watermelon", "cherry", "banana","pineapple"]
# print("List before sorting : ", list_of_strings)
# sorted_list = sorted(list_of_strings, key=lambda x: len(x))
# print("List after sorting : ", sorted_list)






# (4). Use lambda functions with map, filter, and reduce:
# Use map to square a list of numbers.
# Use filter to find all even numbers in a list.
# Use reduce to find the product of a list of numbers (requires functools).

# Ans...

# square_list = [5, 6, 7]
# square_number = map(lambda x: x**2, square_list)
# print(list(square_number))


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(filter(lambda x : (x % 2 == 0),list1))
# print(even_num)


# from functools import reduce
# num = [3, 4, 5, 6]
# product = reduce(lambda x, y: x * y, num)
# print(product)