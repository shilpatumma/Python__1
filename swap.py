# (1). swap value with 3rd variable

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

temp = num1
num1 = num2
num2 = temp

print("Value of num1 : ", num1)
print("Value of num2 : ", num2)



# (2). swap value without 3rd variable

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

num1, num2 = num2, num1

print("Value of num1 : ", num1)
print("Value of num2 : ", num2)