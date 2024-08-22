# (1). Method Overloading :

# class Company:
#     def comp(self,name = None):
#         if name is not None:
#             print("Company name is " + name)
#         else:
#             print("The company has not been named yet!")

# c = Company()
# c.comp()
# c.comp("Infosys")




# (2). Method Overriding :

# class Parent:
#     def parent(self):
#         print("Parent")

# class Child(Parent):
#     def parent(self):
#         print("Child")

# c = Child()
# c.parent()





# Practice Question :

# (1). Python Class with Method Overloading.
# Ans...

# class MyClass:
#     def myclass(self,para1 = None):
#         if para1 is not None:
#             print(para1)
#         else:
#             print("para1 is none")

# m = MyClass()
# m.myclass()
# m.myclass("Parameter 1")
        


# (2). Python Class with Method Overriding.
# Ans...

# class Cat:
#     def cat(self):
#         print("Cat")

# class Kitten(Cat):
#     def kitten(self):
#         print("Kitten")

# k = Kitten()
# k.kitten()
# k.cat()



# (3). Python oops program to create a class with a static method.
# Ans...

# class Calculate:
#     def multiply(a,b):
#         return a * b

# Calculate.multiply = staticmethod(Calculate.multiply)
# mul = (Calculate.multiply(10,10))
# print("The multiplication is :", mul)



# (4). Python oops program to create a class with the class method.
# Ans...

# class Company:
#     name = "Microsoft"

#     def comapny_name(cls):
#         print("Company name is :", cls.name)

# Company.comapny_name = classmethod(Company.comapny_name)
# Company.comapny_name()





# Method Overriding.
# class Animal:
#     def animal(self):
#         print("Animal class")

# class Dog(Animal):
#     def dog(self):
#         print("\nDog class")

# class Cat(Animal):
#     def cat(self):
#         print("\nCat class")

# d = Dog()
# d.dog()
# d.animal()

# c = Cat()
# c.cat()
# c.animal()



# Method Overloading.
# class Tiger:
#     def nature(self):
#         print("\nDangerous")

#     def color(self):
#         print("Orange with black strips")

# class Elephant:
#     def nature(self):
#         print("Calm and harmless")

#     def color(self):
#         print("Grayish black\n")

# t = Tiger()
# e = Elephant()

# for animal in(t, e):
#     animal.nature()
#     animal.color()



