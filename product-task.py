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
# # class Order:
# #     def __init__(self, order_id, customer, items):
# #         self.order_id = order_id
# #         self.customer = customer
# #         self.items = items


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
#     order_id = 0
#     def __init__(self, customer, items):
#         self.customer = customer
#         self.items = items
#         Order.order_id += 1
#         self.order_id = Order.order_id


#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def get_order_details(self):
#         item_details = "\n".join([item.get_product_details() for item in self.items])
#         return f"\n\nOrder ID: {self.order_id}, Customer: {self.customer}, Items: \n{item_details}"

# # Subclass for Domestic Order
# class DomesticOrder(Order):
#     def __init__(self, customer, items, shipping_address):
#         super().__init__(customer, items)
#         self.shipping_address = shipping_address

#     def calculate_shipping_cost(self):
#         # Example flat rate for domestic shipping
#         return 5.00

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}"

# # Subclass for International Order
# class InternationalOrder(Order):
#     def __init__(self, customer, items, shipping_address, customs_duty):
#         super().__init__(customer, items)
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



#     laptop = ElectronicProduct("Laptop", 1200.00, "High-end gaming laptop", "BrandX", 2)
#     tshirt = Clothing("T-shirt", 20.00, "Cotton T-shirt", "L", "Cotton")
#     book = Book("Data Science 101", 30.00, "Introduction to Data Science", "Jane Doe", "Educational")
#     sofa = Furniture("Sofa", 500.00, "Comfortable sofa", "Leather", "7x3 feet")

#     # Creating an order
#     order_items = [laptop, tshirt, book, sofa]
#     domestic_order = DomesticOrder("John Smith", order_items, "123 Main St, Springfield")
#     international_order = InternationalOrder("Jane Doe", order_items, "456 Global St, London", 50.00)


    # order_items = [laptop, tshirt, book, sofa]
    # domestic_order = DomesticOrder("Max", order_items, "123 Main St, Springfield")
    # international_order = InternationalOrder("Bob", order_items, "456 Global St, London", 50.00)

    # # Print order details
    # print(domestic_order.get_order_details())
    # print("\n" + "="*40 + "\n")
    # print(domestic_order.calculate_total())


    # print(international_order.get_order_details())
    # print("\n" + "="*40 + "\n")
    # print(international_order.calculate_total())








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

# from datetime import datetime

# # Account Hierarchy
# class Account:
#     def _init_(self, account_number, customer_name, balance, account_type):
#         self.account_number = account_number
#         self.customer_name = customer_name
#         self.balance = balance
#         self.account_type = account_type

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

#     def get_account_details(self):
#         return f"Account Number: {self.account_number}\nCustomer: {self.customer_name}\nBalance: ${self.balance:.2f}\nAccount Type: {self.account_type}\n"

# # Subclass for Savings Account
# class SavingsAccount(Account):
#     def _init_(self, account_number, customer_name, balance, interest_rate):
#         super()._init_(account_number, customer_name, balance, account_type="Savings")
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate
#         print(f"Interest calculated: ${interest:.2f}")
#         return interest

#     def apply_interest(self):
#         interest = self.calculate_interest()
#         self.deposit(interest)

# # Subclass for Checking Account
# class CheckingAccount(Account):
#     def _init_(self, account_number, customer_name, balance, overdraft_limit):
#         super()._init_(account_number, customer_name, balance, account_type="Checking")
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if amount > self.balance + self.overdraft_limit:
#             print("Overdraft limit exceeded!")
#         else:
#             self.balance -= amount
#             print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

# # Subclass for Fixed Deposit
# class FixedDeposit(Account):
#     def _init_(self, account_number, customer_name, balance, interest_rate, maturity_date):
#         super()._init_(account_number, customer_name, balance, account_type="Fixed Deposit")
#         self.interest_rate = interest_rate
#         self.maturity_date = maturity_date

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate
#         print(f"Interest calculated: ${interest:.2f}")
#         return interest

#     def withdraw(self, amount):
#         if datetime.now().date() < self.maturity_date:
#             print("Cannot withdraw before maturity date!")
#         else:
#             super().withdraw(amount)

#     def get_account_details(self):
#         base_details = super().get_account_details()
#         return f"{base_details}Maturity Date: {self.maturity_date}\nInterest Rate: {self.interest_rate:.2%}\n"

# # Transaction Hierarchy
# class Transaction:
#     def _init_(self, transaction_id, account, amount):
#         self.transaction_id = transaction_id
#         self.account = account
#         self.amount = amount
#         self.date = datetime.now()

#     def process_transaction(self):
#         raise NotImplementedError("Subclasses should implement this method")

#     def get_transaction_details(self):
#         return f"Transaction ID: {self.transaction_id}\nAccount Number: {self.account.account_number}\nAmount: ${self.amount:.2f}\nDate: {self.date}\n"

# # Subclass for Deposit
# class Deposit(Transaction):
#     def process_transaction(self):
#         self.account.deposit(self.amount)
#         print(f"Deposit of ${self.amount:.2f} processed for Account {self.account.account_number}.")

# # Subclass for Withdrawal
# class Withdrawal(Transaction):
#     def process_transaction(self):
#         self.account.withdraw(self.amount)
#         print(f"Withdrawal of ${self.amount:.2f} processed for Account {self.account.account_number}.")

# # Subclass for Transfer
# class Transfer(Transaction):
#     def _init_(self, transaction_id, account, amount, beneficiary_account):
#         super()._init_(transaction_id, account, amount)
#         self.beneficiary_account = beneficiary_account

#     def process_transaction(self):
#         if self.account.balance >= self.amount:
#             self.account.withdraw(self.amount)
#             self.beneficiary_account.deposit(self.amount)
#             print(f"Transfer of ${self.amount:.2f} from Account {self.account.account_number} to Account {self.beneficiary_account.account_number} processed.")
#         else:
#             print("Insufficient funds for transfer!")

#     def get_transaction_details(self):
#         base_details = super().get_transaction_details()
#         return f"{base_details}Beneficiary Account: {self.beneficiary_account.account_number}\n"

# # Example Usage
# if _name_ == "_main_":
#     # Creating accounts
#     savings_account = SavingsAccount("SA12345", "Alice Johnson", 5000.00, interest_rate=0.02)
#     checking_account = CheckingAccount("CA54321", "Bob Smith", 3000.00, overdraft_limit=500.00)
#     fd_account = FixedDeposit("FD67890", "Charlie Brown", 10000.00, interest_rate=0.05, maturity_date=datetime(2025, 12, 31).date())

#     # Printing account details
#     print(savings_account.get_account_details())
#     print(checking_account.get_account_details())
#     print(fd_account.get_account_details())

#     print("\n" + "="*40 + "\n")

#     # Processing transactions
#     deposit = Deposit("TXN001", savings_account, 200.00)
#     deposit.process_transaction()

#     withdrawal = Withdrawal("TXN002", checking_account, 3500.00)
#     withdrawal.process_transaction()

#     transfer = Transfer("TXN003", savings_account, 1000.00, beneficiary_account=checking_account)
#     transfer.process_transaction()

#     # Applying interest on Savings Account
#     savings_account.apply_interest()
        




# (4). Telecommunication System
# Call Hierarchy:
# Base class Call with attributes like caller, callee, start_time, end_time.
# Subclasses: VoiceCall, VideoCall, ConferenceCall, etc., 
# with specific attributes (e.g., video_quality, participants) 
# and methods (e.g., calculate_duration, record_call).

# Customer Hierarchy:
# Base class Customer with attributes like customer_id, name, address.
# Subclasses: IndividualCustomer, CorporateCustomer, etc., with specific attributes (e.g., company_name, tax_id) and methods (e.g., generate_bill).

# Ans...





class Call:
    def __init__(self, caller, callee, start_time, end_time):
        self.caller = caller
        self.callee = callee
        self.start_time = start_time
        self.end_time = end_time

    def calculate_duration(self):
        duration = self.end_time - self.start_time
        return duration


class VoiceCall(Call):
    def __init__(self, caller, callee, start_time, end_time):
        super().__init__(caller, callee, start_time, end_time)

    def record_call(self):
        print(f"Recording voice call : from {self.caller} to {self.callee}")


class VideoCall(Call):
    def __init__(self, caller, callee, start_time, end_time, video_quality):
        super().__init__(caller, callee, start_time, end_time)
        self.video_quality = video_quality

    def record_call(self):
        print(f"Recording video call : from {self.caller} to {self.callee} at {self.video_quality}")


class ConferenceCall(Call):
    def __init__(self, caller, participants, start_time, end_time):
        super().__init__(caller, participants, start_time, end_time)
        self.participants = participants

    def record_call(self):
        print(f"Recording Conference call with participants : {', '.join(self.participants)}")


class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def generate_bill(self):
        return f"\nBill for {self.name} & ID : {self.customer_id}"


class IndividualCustomer(Customer):
    def __init__(self, customer_id, name, address, phone_number):
        super().__init__(customer_id, name, address)
        self.phone_number = phone_number

    def generate_bill(self, charge):
        customer_bill = super().generate_bill()
        self.charge = charge
        return f"{customer_bill} \nPhone Number : {self.phone_number} \nCharge : {self.charge}"


class CorporateCustomer(Customer):
    def __init__(self, customer_id, name, address, company_name, tax_id):
        super().__init__(customer_id, name, address)
        self.company_name = company_name
        self.tax_id = tax_id

    def generate_bill(self, charge):
        customer_bill = super().generate_bill()
        self.charge = charge
        return f"{customer_bill} \nCompany Name : {self.company_name} & Tax ID : {self.tax_id} \ncharge : {self.charge}"

if __name__ == "__main__":
    print("\n************ Telecommunication System ************")

    individual = IndividualCustomer(101, "Priya", "45, new bunglow, Mumbai.", 1234567890)
    corporate = CorporateCustomer(201, "Sunidhi", "78, shine complex, Delhi.", "ABC Tech company", 12345)

    voice_call = VoiceCall("Priya", "Fenil", 0, 240)
    video_call = VideoCall("Priya", "Vivek", 0, 300, "720p")
    conference_call = ConferenceCall("Sunidhi", ["riya", "Kevin", "Jenish"], 0, 360)

    print(f"\nvoice call duration : {voice_call.calculate_duration()} seconds.")
    voice_call.record_call()

    print(f"\nvideo call duration : {video_call.calculate_duration()} seconds.")
    video_call.record_call()

    print(f"\nconference call duration : {conference_call.calculate_duration()} seconds.")
    conference_call.record_call()

    print(individual.generate_bill(150))
    print(corporate.generate_bill(250))








# class Call:
#     def __init__(self, caller, callee, start_time, end_time):
#         self.caller = caller
#         self.callee = callee
#         self.start_time = start_time
#         self.end_time = end_time

#     def calculate_duration(self):
#         duration = self.end_time - self.start_time
#         return duration

# class VoiceCall(Call):
#     def __init__(self, caller, callee, start_time, end_time):
#         super().__init__(caller, callee, start_time, end_time)

#     def record_call(self):
#         print(f"Recording Voice call : from {self.caller} to {self.callee}")

# class VideoCall(Call):
#     def __init__(self, caller, callee, start_time, end_time, video_quality):
#         super().__init__(caller, callee, start_time, end_time)
#         self.video_quality = video_quality

#     def record_call(self):
#         print(f"Recording Video call : from {self.caller} to {self.callee} at {self.video_quality}")

# class ConferenceCall(Call):
#     def __init__(self, caller, participants, start_time, end_time):
#         super().__init__(caller, participants[0], start_time, end_time)
#         self.participants = participants

#     def record_call(self):
#         print(f"Recording Conference call with participants : {', '.join(self.participants)}.")


# class Customer:
#     def __init__(self, customer_id, name, address):
#         self.customer_id = customer_id
#         self.name = name
#         self.address = address

#     def generate_bill(self):
#         return f"\nBill for {self.name} (ID : {self.customer_id})"


# class IndividualCustomer(Customer):
#     def __init__(self, customer_id, name, address, phone_number):
#         super().__init__(customer_id, name, address)
#         self.phone_number = phone_number

#     def generate_bill(self):
#         base_bill = super().generate_bill()
#         return f"{base_bill}\nPhone Number : {self.phone_number}"


# class CorporateCustomer(Customer):
#     def __init__(self, customer_id, name, address, company_name, tax_id):
#         super().__init__(customer_id, name, address)
#         self.company_name = company_name
#         self.tax_id = tax_id

#     def generate_bill(self):
#         base_bill = super().generate_bill()
#         return f"{base_bill}\nCompany Name is : {self.company_name}\nTax ID - {self.tax_id}"


# if __name__ == "__main__":
#     print("\n..........Telecommunication System..........")

#     individual = IndividualCustomer(101, "Pooja Shukla", "89, street road", 1234567890)
#     corporate = CorporateCustomer(201, "Mihir Mehra", "45, New Street", "ABC pvt ltd.", 12345)

#     voice_call = VoiceCall(individual.name, "Manoj Patel", 5, 30)
#     video_call = VideoCall(individual.name, "Chetna Nair", 10, 50, "720p")
#     conference_call = ConferenceCall(corporate.name, ["Sneha", "Bobby", "Kreeva"], 50, 150)

#     print("\nCalls :")
#     print(f"\nVoice Call Duration is : {voice_call.calculate_duration()} seconds")
#     voice_call.record_call()

#     print(f"\nVideo Call Duration is : {video_call.calculate_duration()} seconds")
#     video_call.record_call()

#     print(f"\nConference Call Duration is : {conference_call.calculate_duration()} seconds")
#     conference_call.record_call()

#     print("\nGenerating Bills :")
#     print(individual.generate_bill())
#     print(corporate.generate_bill())






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