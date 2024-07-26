# wap to print harmonic series (1/1, 1/2, 1/3,...1/n) and calculate sum of that series.

num = int(input("\nEnter the number : "))
sum = 0
for i in range(1, num + 1):
    sum += (1/i)
print("The sum of harmonic series is",round(sum,2))