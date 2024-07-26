# salary

basic = int(input("Enter basic salary of an employee : "))


if(basic <= 10000):
    da  = basic * 0.8
    hra = basic * 0.2
    
elif(basic <= 20000):    
    da  = basic * 0.9
    hra = basic * 0.25
    
else:
    da  = basic * 0.95
    hra = basic * 0.3
    

    gross = basic + hra + da

    print("GROSS SALARY OF EMPLOYEE = ", gross)