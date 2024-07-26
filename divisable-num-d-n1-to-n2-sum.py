# wap to calculate sum of all divisible of number d in given n1 to n2 range.

n1 = int(input("\nEnter the first number : "))
n2 = int(input("Enter the second number : "))
divisor = int(input("\nEnter the divisor: "))

total_sum = 0

for number in range(n1, n2 + 1):
    if number % divisor == 0:
        total_sum += number

print("\nThe sum is = ", total_sum)