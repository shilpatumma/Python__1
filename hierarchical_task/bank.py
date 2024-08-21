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
        

