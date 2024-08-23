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





from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

    @abstractmethod
    def details(self):
        pass


class SBI(Bank):
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def details(self):
        print(f"\nBank name :",self.name)
        print(f"Inetrest rate :", sbi.get_interest_rate(),"%")


class HDFC(Bank):
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def details(self):
        print(f"\nBank name :",self.name)
        print(f"Inetrest rate :", hdfc.get_interest_rate(),"%")


class ICICI(Bank):
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def details(self):
        print(f"\nBank name :",self.name)
        print(f"Inetrest rate :", icici.get_interest_rate(),"%")


sbi = SBI("SBI Bank", 8.2)
hdfc = HDFC("HDFC Bank", 7.8)
icici = ICICI("ICICI Bank", 7.4)

sbi.details()
hdfc.details()
icici.details()