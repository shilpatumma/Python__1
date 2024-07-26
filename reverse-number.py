# wap to reverse given input number (ex: 3847 ans: 7483)

n = int(input("\nEnter the integer number: "))  
  
reverse = 0  
  
while (n != 0):  
    remainder = n % 10  
    reverse = (reverse * 10) + remainder  
    n = n // 10  
  
print("The reverse number is :", reverse) 