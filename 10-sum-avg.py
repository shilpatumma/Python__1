# wap to get read 10 input from user and print it's sum and average

print("\nEnter 10 numbers")

i = 0 
sum = 0 

while i < 10:

   n = int(input()) 
   sum = sum + n 
   i += 1 

avg = sum / 10 

print("The sum is ; ",sum)
print("The average is : ",avg)