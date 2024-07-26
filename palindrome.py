# wap to check number is palindrome or not(input: 373 ans: 373(reverse),so it is palindrome)

num = int(input("\nEnter the number : "))
temp = num
rev = 0
while (num != 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if (temp == rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")