# find area of (1) square, (2) circle, (3) rectangle, (4) triangle

# (1) square

s = int(input("Enter value : "))

area_of_square = s * s
print(area_of_square)




# (2) circle
 
pi = 3.14

r = float(input("Enter value : "))

area_of_circle = pi * (r*r)
print(area_of_circle)




# (3) rectangle

rectangleHeight = int(input("Enter first value : "))
rectanglewidth = int(input("Enter second value : "))

area_of_rectangle = rectangleHeight * rectanglewidth

print(area_of_rectangle)




# (4) triangle

triangleBase = int(input("Enter first value : "))
triangleHeight = int(input("Enter first value : "))

area_of_triangle = 1/2 * triangleBase * triangleHeight
print(area_of_triangle)