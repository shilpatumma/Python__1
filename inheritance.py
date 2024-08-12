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




# (3). Multilevel Inheritance :

# class Grandfather:
#     def grandf(self):
#         print("Grand Father")

# class Father(Grandfather):
#     def father(self):
#         print("Father")

# class Son(Father):
#     def son(self):
#         print("Son")

# s = Son()
# s.grandf()
# s.father()
# s.son()



# (4). HIERARCHICAL Inheritance :

# class Parent:
#     def parent(self):
#         print("Parent")

# class Son(Parent):
#     def son(self):
#         print("Son")

# class Daughter(Parent):
#     def daughter(Self):
#         print("Daughter")

# d = Daughter()
# s = Son()

# d.parent()
# d.daughter()

# s.parent()
# s.son()



# (5). Hybrid Inheritance :

# class Parent:
#     def parent(self):
#         print("Parent")

# class Child_1(Parent):
#     def child1(self):
#         print("Child_1")

# class Child_2(Parent):
#     def child2(self):
#         print("Child_2")

# class Grand_child(Child_1,Child_2):
#     def grandchild(self):
#         print("Grandchild")

# gc = Grand_child()
# gc.parent()
# gc.child1()
# gc.child2()
# gc.grandchild()



# Practice Question :

# (1). Python class with Single Inheritance.
# Ans...

# class Vehicle:
#     def vehicle_info(self):
#         print("Vehicle")
# class Car(Vehicle):
#     def car_info(self):
#         print("Car")

# c = Car()
# c.vehicle_info()
# c.car_info()



# (2). Python Class with Multiple Inheritance.
# Ans...

# class Animal:
#     def animal(self):
#         print("Animal")

# class Cat:
#     def cat(self):
#         print("Cat")

# class Dog(Animal,Cat):
#     def dog(self):
#         print("Dog")

# d = Dog()
# d.animal()
# d.cat()
# d.dog()



# (3). Python Class with Multilevel Inheritance.
# Ans...

# class Animal:
#     def animal(self):
#         print("Animal")

# class Cat(Animal):
#     def cat(self):
#         print("Cat")

# class Kitten(Cat):
#     def kitten(self):
#         print("Kitten")

# k = Kitten()
# k.animal()
# k.cat()
# k.kitten()



# (4). Python Class with Hierarchical Inheritance.
# Ans...

# class Animal:
#     def animal(self):
#         print("Animal")

# class Cat1(Animal):
#     def cat1(self):
#         print("Cat1")

# class Cat2(Animal):
#     def cat2(self):
#         print("Cat2")

# c1 = Cat1()
# c1.animal()
# c1.cat1()

# c2 =  Cat2()
# c2.animal()
# c2.cat2()