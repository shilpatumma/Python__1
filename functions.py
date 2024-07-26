# square

# def square(x):
#     return x ** 2
# result = square(5)
# print(result)  


# factorial

# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# result = factorial(5)
# print(result)   


# create a function in python

# def prac (name, age):
#     print(name, age)
# prac("Samiksha", 26)


# create a function with variable length of arguments.

# The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function.

# def prac (*args):
#     for i in args:        
#         print(i)
# prac(1, 2, 3, 4, 5)
# prac(6, 7, 8)


# Return multiple values from a function

# def cal (x, y):
#     addition = x + y
#     substraction = x - y
#     multiplication = x * y
#     division = x / y
#     modulo = x % y

#     return(addition, substraction, multiplication, division, modulo)
# result = cal(10, 5)
# print(result)



# Create a function with a default argument 

# def employee (name, salary = 15000):
#     print("Name is : ", name, ", Salary is : ", salary)
# employee("Vinita", 20000)
# employee("Navya")



# Create a recursive function

# def number (num):
#     if num:
#         return num + number(num - 1)
#     else:
#         return 0 
# result = number(12)
# print(result)



# Practice Question  :

# Operators
# (1). Write a program that takes two numbers as input and performs basic arithmetic operations (+, -, *, /) on them.
# (2). Create a program that calculates the area of a circle given its radius.
# (3). Write a script that converts temperature from Celsius to Fahrenheit and vice versa.

# Ans(1)...

# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

# def mod(num1, num2):
#     return num1 % num2

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))

# print("The Addition is : ",(add(num1, num2)))
# print("The Subtraction is : ",(sub(num1, num2)))
# print("The Multiplication is : ",(mul(num1, num2)))
# print("The Division is : ",(div(num1, num2)))
# print("The Modulus is : ",(mod(num1, num2)))



# Ans(2)...

# def area_of_circle (r):
#     pi = 3.14
#     area = pi * (r*r)
#     return area
# radius = int(input("Enter value : "))
# print("Area is : ",area_of_circle(radius))


# ans (3)...

# f = int(input("\nEnter temperature in fahrenheit : "))
# c = (f - 32) / 1.8
# print(str(f) + " degree Fahrenheit is equal to " + str(c) + " degree Celsius.")





# Conditional Statements
# (4). Write a program that checks if a number is positive, negative, or zero.
# (5). Create a script that determines if a year is a leap year or not.

# Ans (4)...

# num = int(input("\nEnter the number : "))
# if(num > 0):
#     print("The number is positive")
# elif(num < 0):
#     print("The number is negative")
# else:
#     print("The number is zero")



# Ans (5)...

# def leap(year):
#     if(year % 4 == 0):
#         if(year % 100 == 0):
#             if(year % 400 != 0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# year = int(input("Enter the Year : "))
# if(leap(year)):
#     print("Leap Year")
# else:
    # print("Not a Leap Year")




# If-Else and Elif
# (6). Write a program that determines the grade of a student 
     # based on their percentage score.
# (7). Create a script that checks if a number is divisible by 5 and 11 or not.
# (8). Write a program that compares two numbers and displays the larger number.

# Ans (6)...

# def stu_grade(percentage):
#     if 90 <= percentage <= 100:
#         return "A"
#     elif 80 <= percentage < 90:
#         return "B"
#     elif 70 <= percentage < 80:
#         return "C"
#     elif 60 <= percentage < 70:
#         return "D"
#     elif 50 <= percentage < 60:
#         return "F"
#     else:
#         return "FAIL"
# percentage = float(input("Enter the percentage score : "))
# grade = stu_grade(percentage)
# print("The grade is :",grade)


# Ans (7)...

# def div(num):
#     return num % 5 == 0 and num % 7 == 0
# num = int(input("Enter number : "))	
# if(num % 5 == 0 and num % 7 == 0):
# 	print("num is divisible by 5 and 7 \n")
# else:
# 	print("num is not divisible by 5 and 7 \n")	


# Ans (8)...

# def find_max_num(number1, number2):
#     if (number1 > number2):
#         return number1
#     else:
#         return number2
# number1 = int(input("enter first number : "))
# number2 = int(input("enter second number : "))
# larger_number = find_max_num(number1, number2)
# print("The larger number is :",larger_number)



# Loops
# (9). Write a program that prints the first 10 natural numbers using a for loop.
# (10). Create a script that calculates the factorial of a number using a while loop.
# (11). Write a program that prints the multiplication table of a given number.

# Ans (9)...
# def natural_num():
#     for num in range(1, 11):
#         print(num)
# print(natural_num())


# Ans(10)...
# def factorial(n):
#     if n < 0:
#         return "Enter valid number..."
    
#     fact = 1
#     while n > 0:
#         fact = fact * n
#         n = n - 1
    
#     return fact
# number = int(input("Enter the number : "))
# print(f"The factorial is :",factorial(number))


# Ans (11)... 
# def mul_table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n*i)

# num = int(input("Enter the number : "))
# print(mul_table(num))

    

# While Loop
# (12). Write a program that checks if a number is prime or not using a while loop.
# (13). Create a script that reverses a number using a while loop.
# (14). Write a program that checks if a string is a palindrome using a while loop.

# Ans (12)...

# num = int(input("\nEnter the number : "))
# if (num > 1):
#     for i in range(2, num // 2, +1):
#         if(num % i == 0):
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num, "is a prime number")
# else:
#     print(num, "is not a prime number...")


# Ans (13)...

# num = int(input("\nEnter the number : "))
# reverse = 0
# while(num != 0):
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
# print("the reverse number is : ",reverse)


# Ans (14)...

# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

# num = int(input("\nEnetr the number : "))
# temp = num
# reverse = 0
# while(num != 0):
#     digit = num % 10
#     reverse = (reverse * 10) + digit
#     num = num // 10
# if (temp == reverse):
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")



# Break and Continue Statements
# (15). Write a program that uses a break statement to exit a loop when a certain condition is met.
# (16). Create a script that uses a continue statement to skip certain iterations of a loop.
# (17). Write a program that demonstrates the use of both break and continue statements in a nested loop.

# Ans (15)...

# for i in range(1,11):
#     if (i == 6):
#         break
#     print("Number is : ",i)


# Ans (16)...

# for i in range(1,11):
#     if (i == 6):
#         continue
#     print("Number is : ",i)


# Ans (17)...

# for i in range(1,11):
#     if (i == 5):
#         continue
#     if (i == 8):
#         break
#     print(i)