# find min and max of 3 variables

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if(num1>num2):
    
    if(num1>num3):            
        print("num1 is the maximum")
            
    else:
        print("num3 is the maximum") 
            
        
else:
        
    if(num2>num3):            
        print("num2 is the maximum")
        
            
    else:            
        print("num3 is the maximum")