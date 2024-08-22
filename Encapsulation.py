class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name} \nage : {self.age}")

d = Dog("Max", 2)
d.details()