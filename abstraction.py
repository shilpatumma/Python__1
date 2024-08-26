# from abc import ABC
# class Car(ABC):
#     def mileage(self):
#         pass

# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")

# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 20kmph")

# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 35kmph")

# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 40kmph")

# s = Suzuki()
# s.mileage()

# d = Duster()
# d.mileage()

# t = Tesla()
# t.mileage()

# r = Renault()
# r.mileage()




# from abc import ABC
# class Polygon(ABC):
#     def sides(self):
#         pass

# class Triangle(Polygon):
#     def sides(self):
#         print("Triangle has 3 sides")

# class Pentagon(Polygon):
#     def sides(self):
#         print("Pentagon has 5 sides")

# class Hexagone(Polygon):
#     def sides(self):
#         print("Hexagone has 6 sides")

# class Square(Polygon):
#     def sides(self):
#         print("Square has 4 sides")

# t = Triangle()
# t.sides()

# p = Pentagon()
# p.sides()

# h = Hexagone()
# h.sides()

# s = Square()
# s.sides()




# from abc import ABC, abstractmethod
# class Demo(ABC):
#     @abstractmethod
#     def method_1(self):
#         print("Abstract class")
#         return

#     def method_2(self):
#         print("Concrete class")

# class Base(Demo):
#     def method_1(self):
#         super().method_1()
#         return

# b = Base()
# b.method_1()
# b.method_2()





# from abc import ABC, abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def get_interest_rate(self):
#         pass

#     @abstractmethod
#     def details(self):
#         pass


# class SBI(Bank):
#     def __init__(self, name, interest_rate):
#         self.name = name
#         self.interest_rate = interest_rate

#     def get_interest_rate(self):
#         return self.interest_rate

#     def details(self):
#         print(f"\nBank name :",self.name)
#         print(f"Inetrest rate :", sbi.get_interest_rate(),"%")


# class HDFC(Bank):
#     def __init__(self, name, interest_rate):
#         self.name = name
#         self.interest_rate = interest_rate

#     def get_interest_rate(self):
#         return self.interest_rate

#     def details(self):
#         print(f"\nBank name :",self.name)
#         print(f"Inetrest rate :", hdfc.get_interest_rate(),"%")


# class ICICI(Bank):
#     def __init__(self, name, interest_rate):
#         self.name = name
#         self.interest_rate = interest_rate

#     def get_interest_rate(self):
#         return self.interest_rate

#     def details(self):
#         print(f"\nBank name :",self.name)
#         print(f"Inetrest rate :", icici.get_interest_rate(),"%")


# sbi = SBI("SBI Bank", 8.2)
# hdfc = HDFC("HDFC Bank", 7.8)
# icici = ICICI("ICICI Bank", 7.4)

# sbi.details()
# hdfc.details()
# icici.details()




# from abc import ABC, abstractmethod
# class Clothes(ABC):
#     @abstractmethod
#     def get_price(self):
#         pass

#     @abstractmethod
#     def details(self):
#         pass

# class T_shirt(Clothes):
#     def __init__(self, price, color, size):
#         self.price = price
#         self.color = color
#         self.size = size

#     def get_price(self):
#         return self.price    

#     def details(self):
#         print("............Details of T-shirt............")
#         print(f"Price -", self.price)    
#         print(f"Color -", self.color)    
#         print(f"Size -", self.size)    

# class Shirt(Clothes):
#     def __init__(self, price, color, size):
#         self.price = price
#         self.color = color
#         self.size = size

#     def get_price(self):
#         return self.price    

#     def details(self):
#         print("\n............Details of Shirt............")
#         print(f"Price -", self.price)    
#         print(f"Color -", self.color)    
#         print(f"Size -", self.size)    

# tshirt = T_shirt(350, "Black", "M")
# shirt = Shirt(280, "White", "M")

# tshirt.details()
# shirt.details()





# from abc import ABC, abstractmethod
# class IT_Institute(ABC):
#     @abstractmethod
#     def duration(self):
#         pass

#     @abstractmethod
#     def details(self):
#         pass

# class Java(IT_Institute):
#     def __init__(self, course_name, course_duration, fees):
#         self.course_name = course_name
#         self.course_duration = course_duration
#         self.fees = fees

#     def duration(self):
#         return super().duration()
    
#     def  details(self):
#         print("\n............Java Course Details............")
#         print("Cousre name -", self.course_name)
#         print("Cousre Duration -", self.course_duration)
#         print("Fees -", self.fees)

# class Python(IT_Institute):
#     def __init__(self, course_name, course_duration, fees):
#         self.course_name = course_name
#         self.course_duration = course_duration
#         self.fees = fees

#     def duration(self):
#         return super().duration()
    
#     def  details(self):
#         print("\n............Python Course Details............")
#         print("Cousre name -", self.course_name)
#         print("Cousre Duration -", self.course_duration)
#         print("Fees -", self.fees)

# class React(IT_Institute):
#     def __init__(self, course_name, course_duration, fees):
#         self.course_name = course_name
#         self.course_duration = course_duration
#         self.fees = fees

#     def duration(self):
#         return super().duration()
    
#     def  details(self):
#         print("\n............React Course Details............")
#         print("Cousre name -", self.course_name)
#         print("Cousre Duration -", self.course_duration)
#         print("Fees -", self.fees)

# java = Java("Introduction of Java", "6 Months", 6000)
# python = Python("Basic Introduction of Python", "7 Months", 9000)
# react = React("React Course", "6 Month", 10000)

# java.details()
# python.details()
# react.details()