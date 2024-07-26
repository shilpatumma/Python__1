# (1). Datatypes and VariablesTask: 
# Create variables of different data types (integer, float, string, list, tuple, dictionary) and print each of them.
# Ans...

# a = 5
# print(type(a))        # (integer)


# a = 5.5
# print(type(a))        # (float)


# a = "PYTHON"
# print(type(a))        # (string)


# a = [1, 2, 3, 4]
# print(type(a))        # (list)


# a = (1, 2, 3, 4)
# print(type(a))        # (tuple)


# a = {
#     "Name" : "Purva",
#     "ID" : 12
# }
# print(type(a))        # (dictionary)




# (2). Arithmetic Operators Task: 
# Write a Python program that takes two numbers from the user and performs 
# addition, subtraction, multiplication, division, and modulus operations. Print the results.
# Ans...

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# addition = num1 + num2
# subtraction = num1 - num2
# division = num1 / num2
# modulus = num1 % num2

# print("Addition of" ,num1, "and" ,num2, "is : ",addition)
# print("Subtraction of" ,num1, "and" ,num2, "is : ",subtraction)
# print("Division of" ,num1, "and" ,num2, "is : ",division)
# print("Modulus of" ,num1, "and" ,num2, "is : ",modulus)



# (3). Conditional Statements Task: 
# Write a program that asks the user to enter their age. 
# If the age is 18 or above, print "You are an adult." If the age is below 18, print "You are a minor."
# Task: Write a program that checks if a number entered by the user is even or odd using the if-else statement.
# Task: Write a program to compare two numbers entered by the user and print which one is larger or if they are equal using relational operators.

# Ans...

# age = int(input("Enter age : "))
# if (age >= 18):
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# num = int(input("Enter number : "))
# if (num %2 == 0):
#     print(num, "is even number")
# else:
#     print(num, "is odd number")


# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if (num1 > num2):
#     print(num1, "is larger")
# elif (num1 == num2):
#     print(num1,"and", num2, "is equal")
# else:
#     print(num2, "is larger")




# (4). Logical Operators Task: 
# Write a program that asks the user to enter their age and country. 
# Print "Eligible to vote" if the age is 18 or above and the country is "USA", otherwise print "Not eligible to vote
# Ans...

# age = int(input("Enter your age : "))
# country = (input("Enter your country : "))
# if (age >= 18) and (country == "USA"):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")




# (5). While Loop Task: 
# Write a Python program that prints the numbers from 1 to 10 using a while loop.
# Task: Write a program that takes a number as input and prints its factorial using a while loop.
# Ans... 

# i = 1
# while(i < 11):
#     print(i)
#     i += 1


# num = int(input("\nEnter the Number : "))

# fact = 1
# i = 1
# while(i <= num):
#     fact = fact * i
#     i = i+1
# print("Factorial =", fact)




# (6). For Loop
# Task: Write a Python program that prints each character of a string using a for loop.
# Task: Write a program that prints the numbers from 1 to 10 using the range function in a for loop.

# Ans...

# string = "PYTHON"
# for element in range (0, len(string)):
#     print(string[element])


# i = 1
# for i in range (0, 10):
#     i = i + 1
#     print(i)




# (7). List, List Functions, List Comprehension Task:
# Create a list of numbers from 1 to 5. Print the list, its length, and its sum.
# Task: Write a list comprehension to create a new list 
# that contains the squares of numbers from 1 to 5.

# Ans...

# list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(len(list1))
# print(sum(list1))


# square = [x**2 for x in range (1, 6)]
# print(square)



# (8). Tuple, Tuple FunctionTask:
#  Create a tuple with elements 1, 2, 3, 4, 5.Print the tuple and the length of the tuple.

# Ans...

# t1 = (1, 2, 3, 4, 5)
# print(t1)
# print(len(t1))



# (9). Set, Set FunctionTask: 
# Create a set with elements 1, 2, 3, 4, 5. Add an element to the set and print the set.

# Ans...

# s1 = {1, 2, 3, 4, 5}
# print(s1)
# s1.add(6)
# print(s1)



# (10). Dictionary, Dictionary FunctionTask: 
# Create a dictionary with keys "name", "age", "city" and their corresponding values. 
# Print the dictionary.

# Ans...

# d1 = {
#     "name" : "shilpa",
#     "age" : 23,
#     "city" : "surat"
# }
# print(d1)



# (11). Python Built-In FunctionsTask: 
# Use the len(), sum(), max(), min(), and sorted() functions on a list of numbers 
# and print the result

# Ans...

# numbers = [5, 1, 4, 6, 3, 2]
# print(numbers)
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# print(numbers)



# (12). String, String FunctionTask:

# Write a Python program that takes a string input from the user 
# and prints the string in reverse.
# Task: Write a program that counts the number of vowels in a given string.

# Ans...

# string = input("Enter a string : ")
# rev_string = string[::-1]
# print(rev_string)


# user_input = input("Enter a string : ")
# vowels = "aeiouAEIOU"
# count_num_of_vowels = sum(user_input.count(vowel) for vowel in vowels)
# print(count_num_of_vowels)



# (13). Lambda Function, Map, and FilterTask: 

# Write a lambda function that multiplies a number by 2. 
# Use this function with the map() function on a list of numbers.

# Task: Write a lambda function that checks if a number is even. 
# Use this function with the filter() function on a list of numbers.

# Ans...

# num = [2, 4, 6, 8, 10]
# mul_num = list(map(lambda x: x*2, num))
# print(num)
# print(mul_num)


# num = [23, 45, 34, 78, 67, 90]
# even_num = list(filter(lambda x: x%2 == 0, num))
# print(num)
# print(even_num)