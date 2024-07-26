# take 5 subject of students and find total,min,max,grade and result in python

s1 = int(input("\nEnter English subject of marks : "))
s2 = int(input("Enter Gujarati subject of marks : "))
s3 = int(input("Enter Hindi subject of marks : "))
s4 = int(input("Enter Computer subject of marks : "))
s5 = int(input("Enter Mathematics subject of marks : "))

total = s1 + s2 + s3 + s4 + s5 
avg = total / 5
percent = (total / 500) * 100

totalmarks = print("Total Marks is : ", total)
average = print("Average marks is : ", avg)
percentage = print("Percentage is : ", percent)

if(avg>=90):
    print("Grade: A\n")

elif(avg>=80 and avg<90):
    print("Grade: B\n")

elif(avg>=70 and avg<80):
    print("Grade: C\n")

elif(avg>=60 and avg<70):
    print("Grade: D\n")

else:
    print("Grade: F\n")