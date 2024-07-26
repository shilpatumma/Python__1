# Enter sides length of given triangle and check wheather that triangle is valid or not

a = int(input("Enter length of side1 : "))
b = int(input("Enter length of side2 : "))
c = int(input("Enter length of side3 : "))

if((a + b > c) and (a + c > b) and (b + c > a)):
    print("Triangle is valid")
else:
    print("Triangle is not valid")