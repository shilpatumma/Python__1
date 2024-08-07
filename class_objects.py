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




class Book:
    def __init__(self, title, pages, author, publication_date, price, copies_available, checked_out_by):
        self.t = title
        self.p = pages
        self.a = author
        self.pd = publication_date
        self.pr = price
        self.ca = copies_available
        self.cob = checked_out_by

    def checkout(self,name):
        self.cob.append(name)
        self.ca -= 1

    def check_in(self,name):
        self.cob.remove(name)
        self.ca += 1

    def add_copies(self,number):
        self.ca += number

    def remove_copies(self,number):
        self.ca -= number

    def display(self):
        print(self.t)
        print(self.p)
        print(self.a)        
        print(self.pd)
        print(self.pr)
        print(self.ca)
        print(self.cob)

Motivational_book = Book (
        title = "11 Rules For Life", 
        author = "Chetan Bhagat", 
        publication_date = "26 February 2024",
        pages = "256 pages",
        price = 171,
        copies_available = 5,
        checked_out_by = ["Swastika"]
    )

Motivational_book.display()
# book1 = Book("11 Rules For Life", 256, "Chetan Bhagat", "26 February 2024", 171)

# book1.display()