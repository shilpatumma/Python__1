# (1). Introduction to python
# •	Write a Python script that prints the phrase "This is the beginning of the exam" to the console and then prints the current date and time.
# Ans...

# print("\nThis is the beginning of the exam")


# (2). Datatypes and variables
# • (a). Create variables of different data types (integer, float, string, list, dictionary). Print each variable along with its type.
# Ans...

# a = 5
# print(a)
# print(type(a))        # (integer)


# a = 5.5
# print(a)
# print(type(a))        # (float)


# a = "PYTHON"
# print(a)
# print(type(a))        # (string)


# a = [1, 2, 3, 4]
# print(a)
# print(type(a))        # (list)


# a = {
#     "Name" : "Purva",
#     "ID" : 12
# }
# print(a)
# print(type(a))        # (dictionary)


# (b). • Create a list of student names and a corresponding list of their grades. 
# Print each student's name along with their grade. Then, calculate and print the average grade.
# Ans...

# stu_names = ["Pooja", "Aarush", "Sakshi", "Sohan"]

# stu_grades= [80, 90, 98, 78]
# for i in range (len(stu_names)):
#     print(stu_names[i], "- grade", stu_grades[i])

# average = sum(stu_grades) / 4
# print("Average of grade is :", average)



# (3). Arithmetic operators 
# (a). Write a Python program that takes three numbers from the user and calculates the average. 
# If the average is greater than or equal to 50, print "Pass"; otherwise, print "Fail".

# number1 = int(input("\nEnter first number : "))
# number2 = int(input("\nEnter second number : "))
# number3 = int(input("\nEnter third number : "))

# sum = number1 + number2 + number3
# print("sum is : ", sum)

# average = sum // 3
# print("Average of three number is :", average)

# if average >= 50:
#     print("Pass")
# else:
#     print("Fail")


# (b). Write a program to calculate the area of a triangle. 
# Take input for the base and height from the user, and use the formula: Area = 0.5 * base * height.
# Ans...

# triangleBase = int(input("Enter first value : "))
# triangleHeight = int(input("Enter first value : "))

# area_of_triangle = 0.5 * triangleBase * triangleHeight
# print(area_of_triangle)



# (4). Conditional Statements and Logical Operators 
# (a). Write a program that asks the user to enter their age and nationality. 
# Print "Eligible to vote" if the age is 18 or above and the nationality is "Indian". Otherwise, print "Not eligible to vote".
# Ans...

# age = int(input("\nEnter your age : "))
# nationality = (input("Enter your nationality : "))
# if (age >= 18) and (nationality == "Indian"):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")



# (b). Write a program that asks the user to enter a number. If the number is divisible by both 3 and 5, print "FizzBuzz". 
# If it is only divisible by 3, print "Fizz". If it is only divisible by 5, print "Buzz". Otherwise, print the number itself.
# Ans...

# num = int(input("Enter number : "))

# if (num%3==0 and num%5==0):	
# 	print("FizzBuzz\n")	
# elif (num%3==0):
#     print("Fizz")
# elif (num%5==0):
#     print("Buzz")
# else:	
# 	print("num is not divisible by 3 and 5 \n")



# (5). While loop 
# (a). Write a Python program that prints the Fibonacci sequence up to the 10th term using a while loop.
# Ans...

# n = 10

# x, y = 0, 1
# sum = 0

# while (sum < 10):
#     print(x)
#     x, y = y, x + y  
#     sum += 1  



# (b). Write a program that takes a number as input and checks whether it is a prime number using a while loop.
# Ans...

# num = int(input("Enter number : "))
# i = 2
# prime = 0
# while (i<=num/2):    
#     if (num%i == 0):            
#         print("Number is not a prime")
#         break
#     i+=1    
# else:    
#     print("Number is prime")
    


# (6). For Loop and Range 
# (a). Write a Python program that prints each character of the string "EXAMINATION" in reverse order using a for loop.
# Ans...

# string = input("Enter string : ")
# rev_string = string[::-1]
# print(rev_string)


# (b). Write a program that prints all the even numbers between 1 and 50 using the range function in a for loop.
# Ans...

# for i in range(2,51,2):
#     print(i)
#     i+=1
        
    


# (7). List, List Functions, List Comprehension 
# (a). Create a list of numbers from 1 to 10. Print the list, its length, and the list in reverse order without using the reverse function.
# Ans...

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l1)
# print(len(l1))
# print(l1[::-1])



# (b). Write a list comprehension to create a new list that contains only the prime numbers from 1 to 50.
# Ans...

.
.
.
.
.
.

# (c). Given a list of integers, write a program to remove all duplicates and print the list in ascending order.
# Ans...

# l2 = [1, 6, 3, 8, 9, 7, 9, 8]
# print("Original List : ", l2)

# result = list(set(l2))
# print("Aftre remove duplicates : ", result) 

# result.sort()
# print("List in ascending order", result)



# (8). Tuple and Tuple Function 
# (a). Create a tuple with elements representing the first 5 prime numbers. Print the tuple and the sum of the elements.
# Ans...

# t1 = (2, 3, 5, 7, 11)
# print(t1)
# print(sum(t1))



# (b). Write a program to convert the tuple into a list, append the next prime number, and convert it back to a tuple.
# Ans...

# t2 = (2, 3, 5, 7, 11)
# result = list(t2)
# print(result)

# result.append(13)
# print(result)

# r1 = tuple(result)
# print(r1)




# (9). Set and Set Function 
# (a). Create a set with elements "apple", "banana", "cherry". Add an element "date" to the set and print the set.
# Ans...

# s1 = {"apple", "banana", "cherry"}
# s1.add("date")
# print(s1)



# (b). Write a program to find the symmetric difference between two sets: set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}.
# Ans...

# set1 = {1, 2, 3, 4} 
# set2 = {3, 4, 5, 6}

# set3 = set1.symmetric_difference(set2)
# print(set3)



# (10). Dictionary and Dictionary Function
# (a). Create a dictionary with keys "name", "age", "marks" and their corresponding values. Print the dictionary.
# Ans...

# d1 = {
#     "name" : "Sonal",
#     "age" : 23,
#     "marks" : 90
# }
# print(d1)



# (b). Write a program to add a new key-value pair "grade": "A" to the dictionary. 
# Then, update the value of the "marks" key by adding 10 to the existing value.
# Ans...

# d1 = {
#     "name" : "Sonal",
#     "age" : 23,
#     "marks" : 90
# }
# print("Before adding : ", d1)

# d1["grade"]="A"
# print("After adding : ", d1)

# d1["marks"]=10
# print("Aftre changing marks : ", d1)



# (c). Write a program to iterate over the dictionary and print the keys in alphabetical order.
# Ans...

# d2 = {
#     "name" : "Sonal",
#     "age" : 23,
#     "marks" : 90,
#     "grade" : "A"
# }
# for key in sorted(d2.keys()):
#     print(key)




# (11). Python Built-In Functions
# (a). Use the max(), min(), and sorted() functions on a list of numbers [23, 1, 45, 34, 78] and print the results.
# Ans...

# list_num = [23, 1, 45, 34, 78] 
# print(max(list_num))
# print(min(list_num))
# print(sorted(list_num))



# (b). Write a program to find the length of a given list and a given string using the len() function. 
# Additionally, use the sum() function to find the sum of a list of numbers [10, 20, 30, 40, 50].
# Ans...

# l1 = [10, 20, 30, 40, 50]
# length_list = len(l1)
# print("Length of a given list is :", length_list)

# string = "PYTHON LANGUAGE"
# length_string = len(string)
# print("Length of a given string is :", length_string)

# l3 = [10, 20, 30, 40, 50]
# print(sum(l3))





# (12). String, String Function 
# (a). Write a Python program that takes a string input from the user and prints the number of words in the string.
# Ans...

# word = input("Enter a sentence or phrase: ")
# words_string = word.split()

# num_of_words = len(words_string)
# print("Number of words :", num_of_words)



# (b). Write a program that counts the frequency of each character in a given string and prints the result as a dictionary.
# Ans...
.
.
.
.
.
.

# (c). Write a program to check if two given strings are anagrams.
# Ans...

# s1 = input("Enter first string : ")
# s2 = input("Enter second string : ")

# if(sorted(s1) == sorted(s2)):
#     print("The string is ananagram")
# else:
#     print("The string is not an anagram")



# (13). Lambda Function, Map, and Filter 
# (a). Write a lambda function that cubes a number. Use this function with the map() function on a list of numbers [2, 3, 4, 5, 6].
# Ans...

# num = [2, 3, 4, 5, 6]
# cube = list(map(lambda x: x**3, num))
# print(cube)



# (b). Write a lambda function that checks if a number is odd. Use this function with the filter() function on a list of numbers [10, 15, 20, 25, 30].
# Ans...

# num = [10, 15, 20, 25, 30]
# odd_num = list(filter(lambda x: x % 2 != 0, num))
# print(odd_num)



# (c). Write a program to use the map() function to convert a list of temperatures in Celsius [0, 20, 37, 100] to Fahrenheit using the formula F = C * 9/5 + 32.
# Ans...

# cel_temp = [0, 20, 37, 100]

# def cel_to_fahrenheit(celsius):
#     return celsius * 9/5 + 32

# fahrenheit_temp = list(map(cel_to_fahrenheit, cel_temp))

# print("Celsius Temperatures is :", cel_temp)
# print("Fahrenheit Temperatures is :", fahrenheit_temp)