# wap to print sum of given series (1!/n^1 + 2!/n^2 + 3!/n^3 + ....n!/n^n)

n = int(input("\nEnter the value : "))

sum = 0
i = 1
factorial = 1

while (i <= n):
    
    factorial *= i
    sum += factorial / (n ** i)
    i += 1
print("The sum is : ", sum)