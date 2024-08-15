# class Account:
#     def __init__(self, account_number, balance, customer):
#         self.account_number = account_number
#         self.balance = balance
#         self.customer = customer

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount:.2f}. New balance: ${self.balance:.2f}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount:.2f}. New balance: ${self.balance:.2f}")

#     def get_balance(self):
#         return self.balance


# class SavingsAccount(Account):
#     def __init__(self, account_number, balance, customer, interest_rate):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         return interest


# class CheckingAccount(Account):
#     def __init__(self, account_number, balance, customer, overdraft_limit):
#         super().__init__(account_number, balance, customer)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if amount > self.balance + self.overdraft_limit:
#             print("Overdraft limit exceeded!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount:.2f}. New balance: ${self.balance:.2f}")


# class FixedDeposit(Account):
#     def __init__(self, account_number, balance, customer, interest_rate, maturity_date):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate
#         self.maturity_date = maturity_date

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         return interest


# class Transaction:
#     def __init__(self, transaction_id, account, amount, date):
#         self.transaction_id = transaction_id
#         self.account = account
#         self.amount = amount
#         self.date = date

#     # def process_transaction(self):
#     #     raise NotImplementedError("This method should be overridden in subclasses.")


# class Deposit(Transaction):
#     def process_transaction(self):
#         self.account.deposit(self.amount)


# class Withdrawal(Transaction):
#     def process_transaction(self):
#         self.account.withdraw(self.amount)


# class Transfer(Transaction):
#     def __init__(self, transaction_id, account, amount, date, beneficiary_account):
#         super().__init__(transaction_id, account, amount, date)
#         self.beneficiary_account = beneficiary_account

#     def process_transaction(self):
#         if self.account.withdraw(self.amount):
#             self.beneficiary_account.deposit(self.amount)
#             print(f"Transferred {self.amount:.2f} to account {self.beneficiary_account.account_number}.")


# def main():
#     print("Welcome to the Banking System")

#     # Create accounts
#     savings_account = SavingsAccount("SA123", 1000, "Alice", 5)
#     checking_account = CheckingAccount("CA123", 500, "Bob", 200)
#     fixed_deposit = FixedDeposit("FD123", 2000, "Charlie", 4, "2025-01-01")

#     while True:
#         print("\nChoose an action:")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Transfer")
#         print("4. Check Balance")
#         print("5. Calculate Interest (Savings/Fixed Deposit)")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             account_type = input("Enter account type (savings/checking): ").lower()
#             amount = float(input("Enter amount to deposit: "))

#             if account_type == "savings":
#                 transaction = Deposit("T001", savings_account, amount, "2024-08-14")
#                 transaction.process_transaction()
#             elif account_type == "checking":
#                 transaction = Deposit("T002", checking_account, amount, "2024-08-14")
#                 transaction.process_transaction()

#         elif choice == '2':
#             account_type = input("Enter account type (savings/checking): ").lower()
#             amount = float(input("Enter amount to withdraw: "))

#             if account_type == "savings":
#                 transaction = Withdrawal("T003", savings_account, amount, "2024-08-14")
#                 transaction.process_transaction()
#             elif account_type == "checking":
#                 transaction = Withdrawal("T004", checking_account, amount, "2024-08-14")
#                 transaction.process_transaction()

#         elif choice == '3':
#             amount = float(input("Enter amount to transfer: "))
#             transaction = Transfer("T005", checking_account, amount, "2024-08-14", savings_account)
#             transaction.process_transaction()

#         elif choice == '4':
#             account_type = input("Enter account type (savings/checking/fixed): ").lower()
#             if account_type == "savings":
#                 print(f"Savings Account Balance: {savings_account.get_balance():.2f}")
#             elif account_type == "checking":
#                 print(f"Checking Account Balance: {checking_account.get_balance():.2f}")
#             elif account_type == "fixed":
#                 print(f"Fixed Deposit Account Balance: {fixed_deposit.get_balance():.2f}")

#         elif choice == '5':
#             account_type = input("Enter account type (savings/fixed): ").lower()
#             if account_type == "savings":
#                 interest = savings_account.calculate_interest()
#                 print(f"Interest earned on Savings Account: {interest:.2f}")
#             elif account_type == "fixed":
#                 interest = fixed_deposit.calculate_interest()
#                 print(f"Interest earned on Fixed Deposit: {interest:.2f}")

#         elif choice == '6':
#             print("Thank you for using the Banking System!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()














