# Enter the angles of triangles and check that triangle is valid or not

t1 = int(input("Enter angle1 : "))
t2 = int(input("Enter angle2 : "))
t3 = int(input("Enter angle3 : "))

sum = t1 + t2 + t3

if (sum == 180):
    print("Trinagle is valid")
else:
    print("Triangle is not valid")