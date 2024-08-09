# (1). Single Inheritance : 

# class Vehicle:
#     def Vehicle_info(self,driver,wheels):
#         self.d = driver
#         self.w = wheels

# class Car(Vehicle):
#     def car_info(self):
#         print(f"Driver name is {self.d} and wheels is {self.w}")

# car = Car()
# car.Vehicle_info("Naveen", 4) 
# car.car_info()



# (2). Multiple Inheritance :

# class Grand_parent:
#     def par_1(self):
#         print("Grand Parent")
# class Parent:
#     def par_2(self):
#         print("Parent")
# class Child(Grand_parent,Parent):
#     pass

# c = Child()
# c.par_1()
# c.par_2()