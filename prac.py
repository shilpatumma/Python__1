# (1). Armstrong number (0, 1, 153, 370, 371, 407)

# num = int(input("\n Enter the number : "))
# sum = 0
# temp = num

# while (num > 0):
#     digit = num % 10
#     sum += digit * digit * digit
#     num //= 10

# if (temp == sum):
#     print("The number is an armstrong")
# else:
#     print("The number is not an armstrong")




# (2). fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,....)

# n = int(input("\nEnter the number of terms in the Fibonacci series : "))

# x, y = 0, 1
# sum = 0

# while (n > sum):
#     # print(x)
#     x, y = y, x + y  
#     sum += 1  
#     print(x)



# (3). Neon number

# num = int(input("\nEnter the number to check : "))
# sum = 0
# square = num * num

# while (square > 0):
#     digit = square % 10
#     sum = sum + digit
#     square = square // 10

# if (sum == num):
#     print("The number is a neon")
# else:
#     print("The number is not a neon")



# (4). Spy number (132 ---> sum = 1+3+2 = 6, multiplication = 1*3*2 = 6)

# num = int(input("\nEnter the number : "))
# sum = 0
# product = 1
# temp = num

# while (num != 0):
#     digit = num % 10
#     sum = sum + digit
#     product = product * digit
#     num = num // 10

# if (sum == product):
#     print("The number is a spy")
# else:
#     print("The number is not a spy")



# (5). Palindrome number (is a number that remains the same when its digits are reversed.)
# (ex...(373, 11, 141, 12321, 75257, 17, 94, 2002))

# num = int(input("\nEnter the number : "))
# temp = num
# reverse_number = 0

# while (num != 0):
#     digit = num % 10
#     reverse_number = reverse_number * 10 + digit
#     num = num // 10

# if (temp == reverse_number):
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")



# (6). Prime number
# (is a natural number greater than 1 that is not a product of 
# two smaller natural numbers. (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...))

# num = int(input("\nEnter the number : "))
# if(num > 1):
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print("The number is not a prime")
#             break
#     else:
#         print("The number is a prime")     
# else:
#     print("The number is not a prime")



# (7). Factorial Series (is a function that multiplies a number 
# by every number below it till 1.)
# (ex... 5! = 5*4*3*2*1 ==> 120)

# num = int(input("\nEnter number : "))

# factorial = i = 1
# while (i <= num):
#     factorial = factorial*i
#     i+=1
# print("The factorial seies is : ",factorial)



# (8). hrmonic series ()

# num = int(input("\nEnter the number : "))
# sum = 0
# for i in range(1, num + 1):
#     sum += (1/i)
# print("The sum of harmonic series is",round(sum,2))