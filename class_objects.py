# class  Car:
#     def __init__(self, year, color):
#         self.yr = year
#         self.cr = color

#     def display(self):
#         print(f"{self.yr} {self.cr}")

# car1 = Car(2001, "red")
# car2 = Car(2000, "white")

# car1.display()
# car2.display()






# class Book:
#     def __init__(self, title, pages, author, publication_date, price, copies_available, checked_out_by):
#         self.t = title
#         self.p = pages
#         self.a = author
#         self.pd = publication_date
#         self.pr = price
#         self.ca = copies_available
#         self.cob = checked_out_by

#     def display(self):
#         print(self.t)
#         print(self.p)
#         print(self.a)        
#         print(self.pd)
#         print(self.pr)
#         print(self.ca)
#         print(self.cob)

# Motivational_book = Book (
#         title = "11 Rules For Life", 
#         author = "Chetan Bhagat", 
#         publication_date = "26 February 2024",
#         pages = "256 pages",
#         price = 171,
#         copies_available = 5,
#         checked_out_by = "Swastika"
#     )

# Motivational_book.display()




# class Employee:
#     def __init__(self, name, salary):
#         self.n = name
#         self.s = salary

#     def display(self):
#         print("Employee name is :", self.n, "\nand salary is :", self.s)

# emp1 = Employee("Tushar", 50000)
# emp2 = Employee("Mahesh", 60000)

# emp1.display()
# emp2.display()

# 11 Rules For Life
# 256 pages
# Chetan Bhagat
# Publication date : 26 February 2024
# 171





class Bank:
    def __init__(self,account_number,name,initial_balance=0):
        self.acc_num = account_number
        self.n = name
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is : {self.balance}")

    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is : {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"current balance is : {self.balance}")

accounts = []

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Check Bank Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5) : ")

    if (choice == "1"):
        account_number = input("Enter your account number : ")
        name = input("Enter Your name : ")
        account = Bank(account_number,name)
        accounts.append(account)
        print("Congratulations your account created successfully...")

    elif (choice == "2"):
        account_number = input("Enter your account number : ")
        if (account.acc_num == account_number):
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("Account Not Found.")

    elif (choice == "3"):
        account_number = input("Enter your account number : ")
        if (account.acc_num == account_number):
            amount = float(input("Enter deposit amount: "))
            account.withdraw(amount)
        else:
            print("Account Not Found.")

    elif (choice == "4"):
        account_number = input("Enter your account number : ")
        if (account.acc_num == account_number):
            account.check_balance()
        else:
            print("Account Not Found.")

    elif (choice == "5"):
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")





# 1). Python oops program to create a class with the constructor.
# Ans...

# class Student:
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age

#     def display(self):
#         print("Student name is :",self.n) 
#         print("Age is :",self.a)

# s = Student("Sneha", 18)
# s.display()




# 2). Python oops program to create a class with an instance variable.
# Ans...

# class Person:
#     def __init__(self,firstname,lastname):

#         self.fname = firstname
#         self.lname = lastname
    
#     def display(self):
#         print("Hello, my name is",self.fname, self.lname)

# p = Person("Sneha", "Verma")
# p.display()




# 3). Python oops program to create a class with Instance methods.
# Ans...

# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self. age = age 
        
#     def introduce(self): 
#         print(f"Hello, my name is {self.name} and I'm {self. age} years old.")
        
# person1 = Person("Kriya", 20) 
# person1.introduce()




# 4). Python oops program to create a class with class variables and update as id.
# Ans...

# class Person:
#     id = 0
#     def __init__(self,name,age):
#         self.n = name
#         self.a = age
#         Person.id += 1

#     def display(self):
#         print(f"Hello, my name is {self.name} and I'm {self. age} years old.")

# x = Person("Sneha", 20)
# x2 = Person("Suraj", 23)
# print(x2.id)