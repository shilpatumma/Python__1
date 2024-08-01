# (1). check the person salary and cibil score to determine the loan amount using conditional statement
# Ans...

# (2). print leap year by user input using nested conditional statement
# Ans...

# leap_year = int(input("Enter Year : "))
# if leap_year %4 == 0:
#     if leap_year %100 == 0:
#         if leap_year %400 == 0:
#             print(leap_year, "Year is a leap year")
#         else:
#             print(leap_year, "Year is not a leap year")
#     else:
#         print(leap_year, "Year is a leap year")
# else:
#      print(leap_year, "Year is not a leap year")



# (3). print the maximum number of a list using for loop
# Ans...

# num_list = [2, 6, 9, 4, 11, 90]
# max_num = num_list[0]

# for i in num_list:
#     if i > max_num:
#         max_num = i
# print("The maximum number in the list is :", max_num)



# (4). print every prime number in 1 to 100 range using for loop
# Ans...

# def prime_num(number):
#     if number <= 1:
#         return False
#     for i in range(2, (num//2)+1):
#         if number % i == 0:
#             return False
#     return True

# for num in range(1, 101):
#     if prime_num(num):
#         print(num, "is prime number")



# (5). iterate through a list using while loop and use break and continue statement for specific values.
# Ans...

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# index_num = 0

# while index_num < len(num):
#     number = num[index_num]

#     if number % 2 == 0:
#         index_num += 1
#         continue

#     if number == 9:
#         break

#     print("odd number is :", number)
#     index_num += 1



# (6). reverse a inputed string using while loop 
# Ans...

# s = input("\nEnter the string : ")
# reverse = ""
# count = len(s)

# while count > 0:
#     reverse = reverse + s[count - 1]
#     count = count - 1

# print("reverse string is : ", reverse)



# (7). print a string is palindrome using while loop
# Ans...





# (8). check if printed number is palindrome using while loop
# Ans... 

# num = int(input("\nEnter the number : "))

# temp = num
# rev = 0

# while (num != 0):
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if (temp == rev):
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")



# (9). create a function to print prime numbers of a specific range 
# Ans...

# def prime_num(number):
#     if number <= 1:
#         return False
#     for i in range(2, (num//2)+1):
#         if number % i == 0:
#             return False
#     return True

# for num in range(1, 20):
#     if prime_num(num):
#         print(num, "is prime number")



# (10). create a function to check the GCD (greatest common divisior) of two number
# Ans...



