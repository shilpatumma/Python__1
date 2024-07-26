# find min and max of 5 variables 

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter fourth number : "))
num5 = int(input("Enter fifth number : "))

    
if(num1 > num2):    
        if (num1>num3):        
            if (num1>num4):            
                if (num1>num4):
                    print("num1 is max")
                
                else:
                    print("num5 is max")            
            
            else:  
                if (num4>num5):
                    print("num4 is max")
                
                else:
                    print("num5 is max")
        
        
        else:         
                if (num3>num5): 
                    print("num3 is max")
                
                else:
                    print("num5 is max")
                
           
                if (num4>num5):
                    print("num4 is max")
                
                else:
                    print("num5 is max")
                
    

else:
            if (num2>num4):
                if (num2>num5):
                    print("num2 is max")
            
                else: 
                    print("num5 is max")
                
            
            else:
                if (num4>num5): 
                    print("num4 is max")
                
                else:
                    print("num5 is max")
                
        
        
            
                if (num3>num5):
                    print("num3 is max")
                
                else:
                    print("num5 is max")
                
           
                if (num4>num5): 
                    print("num4 is max")
                
                else:
                    print("num5 is max")
                
    
# max=a>b?a>c?a>d?a>e?a:e:d>e?d:e:c>d?c>e?c:e:d>e?d:e:b>c?b>d?b>e?b:e:d>e?d:e:c>d?c>e?c:e:d>e?d:e;