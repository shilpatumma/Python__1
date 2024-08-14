# (1). E-commerce Platform
# Product Hierarchy:
# Base class Product with attributes like name, price, description.
# Subclasses: ElectronicProduct, Clothing, Book, Furniture, etc., with specific attributes (e.g., brand, size, author, material) and methods (e.g., calculate_discount, get_product_details).
# Order and Shipping:
# Base class Order with attributes like order_id, customer, items.
# Subclasses: DomesticOrder, InternationalOrder with specific attributes (e.g., shipping_address, customs_duty) and methods (e.g., calculate_shipping_cost).

# Ans...

# # Product Hierarchy
# class Product:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description

#     def calculate_discount(self, discount_rate):
#         return self.price * (1 - discount_rate)

#     def get_product_details(self):
#         return f"Name: {self.name}, Price: ${self.price:.2f}, Description: {self.description}"

# # Subclass for Electronics
# class ElectronicProduct(Product):
#     def __init__(self, name, price, description, brand, warranty):
#         super().__init__(name, price, description)
#         self.brand = brand
#         self.warranty = warranty

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Brand: {self.brand}, Warranty: {self.warranty} years"

# # Subclass for Clothing
# class Clothing(Product):
#     def __init__(self, name, price, description, size, fabric):
#         super().__init__(name, price, description)
#         self.size = size
#         self.fabric = fabric

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Size: {self.size}, Fabric: {self.fabric}"

# # Subclass for Book
# class Book(Product):
#     def __init__(self, name, price, description, author, genre):
#         super().__init__(name, price, description)
#         self.author = author
#         self.genre = genre

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Author: {self.author}, Genre: {self.genre}"

# # Subclass for Furniture
# class Furniture(Product):
#     def __init__(self, name, price, description, material, dimensions):
#         super().__init__(name, price, description)
#         self.material = material
#         self.dimensions = dimensions

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Material: {self.material}, Dimensions: {self.dimensions}"

# # Order and Shipping
# class Order:
#     def __init__(self, order_id, customer, items):
#         self.order_id = order_id
#         self.customer = customer
#         self.items = items

#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def get_order_details(self):
#         item_details = "\n".join([item.get_product_details() for item in self.items])
#         return f"\nOrder ID: {self.order_id}, Customer: {self.customer}, Items: \n{item_details}"

# # Subclass for Domestic Order
# class DomesticOrder(Order):
#     def __init__(self, order_id, customer, items, shipping_address):
#         super().__init__(order_id, customer, items)
#         self.shipping_address = shipping_address

#     def calculate_shipping_cost(self):
#         # Example flat rate for domestic shipping
#         return 5.00

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}"

# # Subclass for International Order
# class InternationalOrder(Order):
#     def __init__(self, order_id, customer, items, shipping_address, customs_duty):
#         super().__init__(order_id, customer, items)
#         self.shipping_address = shipping_address
#         self.customs_duty = customs_duty

#     def calculate_shipping_cost(self):
#         # Example rate for international shipping
#         return 20.00 + self.customs_duty

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}, Customs Duty: ${self.customs_duty:.2f}"

# # Example Usage
# if __name__ == "__main__": 
#     # Creating products
#     laptop = ElectronicProduct("Laptop", 1200.00, "High-end gaming laptop", "BrandX", 2)
#     tshirt = Clothing("T-shirt", 20.00, "Cotton T-shirt", "L", "Cotton")
#     book = Book("Data Science 101", 30.00, "Introduction to Data Science", "Jane Doe", "Educational")
#     sofa = Furniture("Sofa", 500.00, "Comfortable sofa", "Leather", "7x3 feet")

#     # Creating an order
#     order_items = [laptop, tshirt, book, sofa]
#     domestic_order = DomesticOrder(1, "John Smith", order_items, "123 Main St, Springfield")
#     international_order = InternationalOrder(2, "Jane Doe", order_items, "456 Global St, London", 50.00)

#     # Print order details
#     print(domestic_order.get_order_details())
#     print("\n" + "="*40 + "\n")
#     print(domestic_order.calculate_total())





# (2). Human Resources Management System (HRMS)
# Employee Hierarchy:
# Base class Employee with attributes like employee_id, name, salary.
# Subclasses: Manager, Developer, Salesperson, HR, etc., with specific attributes 
# (e.g., department, role, commission) and methods (e.g., calculate_bonus, generate_payslip).
# Leave Management:
# Base class Leave with attributes like employee, start_date, end_date.
# Subclasses: SickLeave, CasualLeave, PaternityLeave, etc., with specific attributes 
# (e.g., medical_certificate, reason) and methods (e.g., approve_leave).

# Ans...


# class Employee:
#     def __init__(self, employee_id, name, salary):
#         self.employee_id = employee_id
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return self.salary * 0.2

#     def generate_payslip(self):
#         return f"\nEmployee Name : {self.name} \nID : {self.employee_id} \nSalary : {self.salary} \nBonus : {self.calculate_bonus()}" 


# class Manager(Employee):
#     def __init__(self, employee_id, name, salary, department):
#         super().__init__(employee_id, name, salary)
#         self.department = department

#     def calculate_bonus(self):
#         return self.salary * 0.25

# class Developer(Employee):
#     def __init__(self, employee_id, name, salary, programming_language):
#         super().__init__(employee_id, name, salary)
#         self.programming_language = programming_language

#     def calculate_bonus(self):
#         return self.salary * 0.3


# class Salesperson(Employee):
#     def __init__(self, employee_id, name, salary, commision):
#         super().__init__(employee_id, name, salary)
#         self.commision = commision

#     def calculate_bonus(self):
#         return self.salary * 0.2 + self.commision

# class HR(Employee):
#     def __init__(self, employee_id, name, salary, role):
#         super().__init__(employee_id, name, salary)
#         self.role = role

#     def calculate_bonus(self):
#         return self.salary * 0.2 
    

# class Leave:
#     def __init__(self, employee, start_date, end_date):
#         self.employee = employee
#         self.start_date = start_date
#         self.end_date = end_date

#     def approval_leave(self):
#         return f"Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"


# class SickLeave(Leave):
#     def __init__(self, employee, start_date, end_date, medical_certificate):
#         super().__init__(employee, start_date, end_date)
#         self.medical_certificate = medical_certificate

#     def approval_leave(self):
#         if self.medical_certificate:
#             return f"\nSick Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"
#         else:
#             return f"\nSick leave denied for {self.employee.name} due to missing medical certificate."


# class CasualLeave(Leave):
#     def __init__(self, employee, start_date, end_date, reason):
#         super().__init__(employee, start_date, end_date)
#         self.reason = reason

#     def approval_leave(self):
#         return f"\nCasual Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"


# class PaternityLeave(Leave):
#     def __init__(self, employee, start_date, end_date, child_certificte):
#         super().__init__(employee, start_date, end_date) 
#         self.child_certificte = child_certificte

#     def approval_leave(self):
#         if self.child_certificte:
#             return f"\nPaternity Leave request approved for {self.employee.name} from {self.start_date} to {self.end_date}"
#         else:
#             return f"\nPaternity leave denied for {self.employee.name} due to missing certificate."


# manager = Manager(1, "Manish Shukla", 90000, "IT")
# developer = Developer(2, "Shivani Mehra", 85000, "Python")
# salesperson = Salesperson(3, "Jyoti Mehta", 80000, 2000)
# hr = HR(4, "Sundar Verma", 75000, "Hiring Employees")


# print(manager.generate_payslip())
# print(developer.generate_payslip())
# print(salesperson.generate_payslip())
# print(hr.generate_payslip())


# sickleave = SickLeave(developer, "14-08-2024", "20-08-2024", medical_certificate = True)
# casualleave = CasualLeave(manager, "16-08-2024", "20-08-2024", reason = "Family events")
# paternityleave = PaternityLeave(salesperson, "17-08-2024", "26-08-2024", child_certificte=True)


# print(sickleave.approval_leave())
# print(casualleave.approval_leave())
# print(paternityleave.approval_leave())






# (3). Banking System
# Account Hierarchy:
# Base class Account with attributes like account_number, balance, customer.
# Subclasses: SavingsAccount, CheckingAccount, FixedDeposit, etc., 
# with specific attributes (e.g., interest_rate, maturity_date) and methods (e.g., calculate_interest, withdraw).

# Transaction Hierarchy:
# Base class Transaction with attributes like transaction_id, account, amount, date.
# Subclasses: Deposit, Withdrawal, Transfer, etc., 
# with specific attributes (e.g., beneficiary_account) and methods (e.g., process_transaction).

# Ans...

# Account
class Account:
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.balance += amount
        return f"\nDeposited {amount}. \nNew balance is : {self.balance}"

    def withdraw(self, amount):   
        if amount <= self.balance:            
            self.balance -= amount 
            return f"\nWithdraw {amount}. \nNew balance is : {self.balance}"
        else:
            return "Insufficient Amount."

    def get_balance(self):
        return f"Current balance : {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer, interest_rate):
        super().__init__(account_number, balance, customer)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"\nInterest added : {interest}. \nNew balance is : {self.balance}"


saving_account = SavingsAccount(101, 5000, "Shivani Mishra", 0.05)
print(saving_account.get_balance())
print(saving_account.deposit(2000))
print(saving_account.calculate_interest())
print(saving_account.withdraw(1000))


# class CheckingAccount(Account):
#     def __init__(self, account_number, balance, customer):
#         super().__init__(account_number, balance, customer)

# class FixedDeposit(Account):
#     def __init__(self, account_number, balance, customer, maturity_date):
#         super.__init__(account_number, balance, customer)
#         self.maturity_date = maturity_date
 

# Transaction
# class Transaction:
#     def __init__(self, transaction_id, account, amount, date):
#         self.transaction_id = transaction_id
#         self.account = account
#         self.amount = amount
#         self.date = date

#     def process_transaction(self):

# class Deposit(Transaction):
#     def __init__(self, transaction_id, account, amount, date):
#         super().__init__(transaction_id, account, amount, date)


# class Withdrawal(Transaction):
#     def __init__(self, transaction_id, account, amount, date):
#         super().__init__(transaction_id, account, amount, date)


# class Transfer(Transaction):
#     def __init__(self, transaction_id, account, amount, date, beneficiary_account):
#         super().__init__(transaction_id, account, amount, date)
#         self.beneficiary_account = beneficiary_account











# (5). Inventory Management System
# Product Hierarchy:
# Base class Product with attributes like product_id, name, price, quantity.
# Subclasses: ElectronicProduct, Clothing, Food, etc., 
# with specific attributes (e.g., warranty, size, expiry_date) 
# and methods (e.g., calculate_discount, check_stock).

# Order Hierarchy:
# Base class Order with attributes like order_id, customer, items.
# Subclasses: PurchaseOrder, SalesOrder, ReturnOrder, etc., 
# with specific attributes (e.g., supplier, reason_for_return) 
# and methods (e.g., process_order, generate_invoice).

# Ans...

# class Product:
#     def __init__(self, product_id, name, price, quantity): 
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def check_stock(self):
#         return self.quantity 

#     def calculate_discount(self):
#         return self.price * 0.3
    
#     def __str__(self):
#         return f"\n{self.name} \nProduct ID : {self.product_id} \nPrice : ${self.price} \nQuantity : {self.quantity}"


# class ElectronicProduct(Product):
#     def __init__(self, product_id, name, price, quantity, warranty):
#         super().__init__(product_id, name, price, quantity)
#         self.warranty = warranty
#     # def calculate_discount(self):
#     #     return self.price * 0.2
        
#     def __str__(self):
#         return super().__str__() + f" \nWarranty: {self.warranty} years"


# class Clothing(Product):
#     def __init__(self, product_id, name, price, quantity, size):
#         super().__init__(product_id, name, price, quantity)
#         self.size = size

#     # def calculate_discount(self):
#     #     return self.price * 0.4
    
#     def __str__(self):
#         return super().__str__() + f" \nSize: {self.size}"
    

# class Food(Product):
#     def __init__(self, product_id, name, price, quantity, expiry_date):
#         super().__init__(product_id, name, price, quantity)
#         self.expiry_date = expiry_date

#     # def calculate_discount(self):
#     #     return self.price * 0.3
        
#     def __str__(self):
#         return super().__str__() + f" \nExpiry Date: {self.expiry_date}"


# class Order:
#     def __init__(self, order_id, customer, items):
#         self.order_id = order_id
#         self.customer = customer
#         self.items = items

#     def process_order(self):
#         for item in self.items:
#             if item.check_stock():
#                 item.quantity -= 1  
#             else:
#                 print(f"Item {item.name} is out of stock!")

#     def generate_invoice(self):
#         total = sum(item.price for item in self.items)
#         invoice_details = f"\nInvoice for Order ID : {self.order_id}\nCustomer Name : {self.customer}\nItems :\n"
#         for item in self.items:
#             invoice_details += f"-> {item.name}: ${item.price}\n"
#         invoice_details += f"\nTotal Amount is : ${total}"
#         return invoice_details

#     def get_order_details(self):
#         item_details = "\n".join([item.get_product_details() for item in self.items])
#         return f"\nOrder ID : {self.order_id}, Customer : {self.customer}, Items : \n{item_details}"

# class PurchaseOrder(Order):
#     def __init__(self, order_id, customer, items, supplier):
#         super().__init__(order_id, customer, items)
#         self.supplier = supplier

#     def __str__(self):
#         return f"Purchase Order ID : {self.order_id}, Supplier : {self.supplier}"


# class SalesOrder(Order):
#     def __init__(self, order_id, customer, items):
#         super().__init__(order_id, customer, items)

#     def __str__(self):
#         return f"Sales Order ID : {self.order_id}, Customer Name : {self.customer}"

# class ReturnOrder(Order):
#     def __init__(self, order_id, customer, items, reason_for_return):
#         super().__init__(order_id, customer, items)
#         self.reason_for_return = reason_for_return

#     def __str__(self):
#         return f"\nReturn Order ID : {self.order_id}, Reason for returning : {self.reason_for_return}"
    


# mobile = ElectronicProduct(1, "Mobile", 715.14, 2, 4)
# shirt = Clothing(2, "Shirt", 10.13, 4, "M")
# mango = Food(3, "Mango", 0.1, 20, "10-10-2024")

# print(mobile)
# print(shirt)
# print(mango)

# order_items = [mobile, shirt, mango]
# sales_order = SalesOrder(101, "Neha Shukla", order_items)

# sales_order.process_order()

# print(sales_order.generate_invoice())

# return_order = ReturnOrder(156, "Max Smith", [shirt], "Size too small")
# print(return_order)