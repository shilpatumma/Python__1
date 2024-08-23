# class Dog:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

#     def details(self):
#         print(f"Name : {self.name} \nage : {self.age}")

# d = Dog("Max", 2)
# d.details()




# Encapsulation :
# class Edureka:
#     def _init_(self):
#         self.course = "Python Programming course"
#         self.duration = "6 Month"

#     def details(self):
#         return self.course + self.duration
    
# e = Edureka()
# print(e.course)
# print(e.duration)
# print(e.details())




# Encapsulation Protected:
# class Edureka:
#     def _init_(self):
#         self.course = "Python Programming course"
#         self._duration = "6 Month"

#     def details(self):
#         return self.course + self._duration
    
# e = Edureka()
# print(e.course)
# print(e._duration)
# print(e.details())



 
# Encapsulation Private :
# class Edureka:
#     def _init_(self):
#         self.course = "Python Programming course"
#         self.__duration = "6 Month"

#     def details(self):
#         return self.course + self.__duration
    
# e = Edureka()
# print(e.course)
# print(e.__duration)
# print(e.details())                           # AttributeError




# Encapsulation Private :
# class Edureka:
#     def _init_(self):
#         self.course = "Python Programming course"
#         self.__duration = "6 Month"

#     def details(self):
#         return self.course + self.__duration
    
# e = Edureka()
# print(e.course)
# print(e.Edureka_duration)
# print(e.details())