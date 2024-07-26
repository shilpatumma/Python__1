# wap to print sum of given series (n^1 - n^2 + n^3 - n^4....n^n)

n = int(input("\nEnter the value of n : "))

sum = 0
i = 1

while (i <= n):
    if (i % 2 == 0):
        sum -= n ** i
    else:
        sum += n ** i
    i += 1

print("The sum is : ", sum)