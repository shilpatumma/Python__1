# check the n1 is divisable by d1 and d2 or not.

n1 = int(input("Enter number : "))

d1 = int(input("Enter first divisable number : "))
d2 = int(input("Enter second divisable number : "))

if (n1%d1==0 and n1%d2==0):
    print("n1 is divisible by d1 and d2 \n")

else:
    print("n1 is not divisible by d1 and d2 \n")