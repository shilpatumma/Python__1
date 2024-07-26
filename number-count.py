# wap to count number of digits in given input (ex: input- 8374 ans- 4)

n = int(input("\nEnter the number : "))
count_number = 0

while (n != 0):
    n //= 10
    count_number += 1

print("Number of digits is : ", count_number)