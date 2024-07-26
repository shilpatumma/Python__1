# wap to check that given number is neon number or not.

num = int(input("\nEnter the number to check : "))

sum = 0
square = num * num

while (square != 0):
    digit = square % 10
    sum = sum + digit
    square = square // 10

if (num == sum):
    print("The number is a neon")
else:
    print("The number is not a neon")