# wap to print n odd numbers and their sum.

n = int(input("\nEnter the number : "))

sum_of_odd_numbers = 0  

print("\nThe odd numbers are : ")

for i in range(n):
    number = 2 * i + 1  
    print(number)  
    sum_of_odd_numbers += number  

print("\nThe sum is : ",sum_of_odd_numbers)