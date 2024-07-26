# wap to check that inputed 3 digit number is armstrong or not.

# n = int(input("\nEnter the number : "))
# sum = 0
# temp = n
# while (n != 0):
    
#         r = n % 10
#         sum = sum + r * r * r
#         n = n // 10
    
# if (sum == temp):
#     print("The number is an Armstrong")
# else:
#     print("The number is not an Armstrong")

    
num = int(input("\nEnter a number: "))
sum = 0
temp = num

while (num > 0):
   digit = num % 10
   sum = sum + digit * digit * digit
   num //= 10 

if (temp == sum):
   print("is an Armstrong number")
else:
   print("is not an Armstrong number")


