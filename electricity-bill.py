# write a program to calculate electricity bill based on used unit.

unit = int(input("Enter the units consumed = "))

if(unit>=0):
		bill=unit*8.00
		print("Electricity Bill in Rupees" ,bill)
	
else:
		print("Please enter valid consumed units...")