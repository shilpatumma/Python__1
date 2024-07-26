# wap to check that input number is spy or not.

num = int(input("\nEnter your number "))
sum = 0
product = 1
temp = num

while (num != 0):
    digit = num % 10
    sum = sum + digit
    product = product * digit
    num = num // 10

if (sum == product):
    print("The number is a Spy")
else:
    print("The number is not a Spy")