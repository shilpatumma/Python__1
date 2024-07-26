# wap to print fibonacci series (1,1,2,3,5,8,13,...)

n = int(input("\nEnter the number of terms in the Fibonacci series: "))

x, y = 0, 1
sum = 0

while (sum < n):
    print(x)
    x, y = y, x + y  
    sum += 1  