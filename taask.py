class Account:
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance



class SavingsAccount(Account):
    def __init__(self, account_number, balance, customer, interest_rate):
        super().__init__(account_number, balance, customer)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest earned: {interest}")
        return interest



class CheckingAccount(Account):
    def __init__(self, account_number, balance, customer, overdraft_limit):
        super().__init__(account_number, balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded.")



class FixedDeposit(Account):
    def __init__(self, account_number, balance, customer, interest_rate, maturity_date):
        super().__init__(account_number, balance, customer)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest earned on FD: {interest}")
        return interest



class Transaction:
    def __init__(self, transaction_id, account, amount, date):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.date = date

    def process_transaction(self):
        raise NotImplementedError("This method should be overridden in subclasses.")



class Deposit(Transaction):
    def process_transaction(self):
        self.account.deposit(self.amount)
        print(f"Transaction ID: {self.transaction_id} - Deposit of {self.amount} processed.")



class Withdrawal(Transaction):
    def process_transaction(self):
        self.account.withdraw(self.amount)
        print(f"Transaction ID: {self.transaction_id} - Withdrawal of {self.amount} processed.")



class Transfer(Transaction):
    def __init__(self, transaction_id, from_account, to_account, amount, date):
        super().__init__(transaction_id, from_account, amount, date)
        self.to_account = to_account

    def process_transaction(self):
        if self.account.withdraw(self.amount):
            self.to_account.deposit(self.amount)
            print(f"Transaction ID: {self.transaction_id} - Transfer of {self.amount} to account {self.to_account.account_number} processed.")


# Creating accounts
savings = SavingsAccount("S001", 1000, "Alice", 5)
checking = CheckingAccount("C001", 500, "Bob", 200)
fd = FixedDeposit("FD001", 3000, "Charlie", 6, "2025-12-31")

# Creating transactions
deposit = Deposit("T001", savings, 200, "2024-08-14")
withdrawal = Withdrawal("T002", checking, 100, "2024-08-14")
transfer = Transfer("T003", checking, savings, 50, "2024-08-14")

# Processing transactions
deposit.process_transaction()
withdrawal.process_transaction()
transfer.process_transaction()

# Checking balances
print(f"Savings Account Balance: {savings.get_balance()}")
print(f"Checking Account Balance: {checking.get_balance()}")
print(f"Fixed Deposit Account Balance: {fd.get_balance()}")
















# class Account:
#     def __init__(self, account_number, balance, customer):
#         self.account_number = account_number
#         self.balance = balance
#         self.customer = customer

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds.")

# class SavingsAccount(Account):
#     def __init__(self, account_number, balance, customer, interest_rate):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest earned: {interest}")
#         return interest

# class CheckingAccount(Account):
#     def __init__(self, account_number, balance, customer, overdraft_limit):
#         super().__init__(account_number, balance, customer)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Overdraft limit exceeded.")

# class FixedDeposit(Account):
#     def __init__(self, account_number, balance, customer, interest_rate, maturity_date):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate
#         self.maturity_date = maturity_date

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest earned on fixed deposit: {interest}")
#         return interest



# class Transaction:
#     def __init__(self, transaction_id, account, amount):
#         self.transaction_id = transaction_id
#         self.account = account
#         self.amount = amount
#         self.date = self.get_current_date()

#     def get_current_date(self):
#         # Simple date representation (YYYY-MM-DD)
#         from datetime import datetime
#         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# class Deposit(Transaction):
#     def process_transaction(self):
#         self.account.deposit(self.amount)

# class Withdrawal(Transaction):
#     def process_transaction(self):
#         self.account.withdraw(self.amount)

# class Transfer(Transaction):
#     def __init__(self, transaction_id, from_account, to_account, amount):
#         super().__init__(transaction_id, from_account, amount)
#         self.to_account = to_account

#     def process_transaction(self):
#         if self.amount <= self.account.balance:
#             self.account.withdraw(self.amount)
#             self.to_account.deposit(self.amount)
#             print(f"Transferred: {self.amount} from {self.account.account_number} to {self.to_account.account_number}.")
#         else:
#             print("Insufficient funds for transfer.")



# def main():
#     accounts = {}
#     transaction_id = 1
    
#     while True:
#         print("\n1. Create Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Transfer Money")
#         print("5. Calculate Interest")
#         print("6. Exit")
        
#         choice = input("Choose an option: ")
        
#         if choice == '1':
#             acc_type = input("Enter account type (savings/checking/fixed): ").strip().lower()
#             account_number = input("Enter account number: ")
#             balance = float(input("Enter initial balance: "))
#             customer = input("Enter customer name: ")
            
#             if acc_type == 'savings':
#                 interest_rate = float(input("Enter interest rate: "))
#                 accounts[account_number] = SavingsAccount(account_number, balance, customer, interest_rate)
#             elif acc_type == 'checking':
#                 overdraft_limit = float(input("Enter overdraft limit: "))
#                 accounts[account_number] = CheckingAccount(account_number, balance, customer, overdraft_limit)
#             elif acc_type == 'fixed':
#                 interest_rate = float(input("Enter interest rate: "))
#                 maturity_date = input("Enter maturity date (YYYY-MM-DD): ")
#                 accounts[account_number] = FixedDeposit(account_number, balance, customer, interest_rate, maturity_date)
#             else:
#                 print("Invalid account type.")

#         elif choice == '2':
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter amount to deposit: "))
#             if account_number in accounts:
#                 Deposit(transaction_id, accounts[account_number], amount).process_transaction()
#             else:
#                 print("Account not found.")

#         elif choice == '3':
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter amount to withdraw: "))
#             if account_number in accounts:
#                 Withdrawal(transaction_id, accounts[account_number], amount).process_transaction()
#             else:
#                 print("Account not found.")

#         elif choice == '4':
#             from_account_number = input("Enter your account number: ")
#             to_account_number = input("Enter beneficiary account number: ")
#             amount = float(input("Enter amount to transfer: "))
#             if from_account_number in accounts and to_account_number in accounts:
#                 Transfer(transaction_id, accounts[from_account_number], accounts[to_account_number], amount).process_transaction()
#             else:
#                 print("One or both accounts not found.")

#         elif choice == '5':
#             account_number = input("Enter account number: ")
#             if account_number in accounts:
#                 if isinstance(accounts[account_number], SavingsAccount):
#                     accounts[account_number].calculate_interest()
#                 elif isinstance(accounts[account_number], FixedDeposit):
#                     accounts[account_number].calculate_interest()
#                 else:
#                     print("Interest calculation not applicable for this account type.")
#             else:
#                 print("Account not found.")

#         elif choice == '6':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid option. Please try again.")

# if __name__ == "__main__":
#     main()










# class Account:
#     def __init__(self, account_number, balance, customer):
#         self.account_number = account_number
#         self.balance = balance
#         self.customer = customer

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds.")

# class SavingsAccount(Account):
#     def __init__(self, account_number, balance, customer, interest_rate):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest earned: {interest}")
#         return interest

# class CheckingAccount(Account):
#     def __init__(self, account_number, balance, customer, overdraft_limit):
#         super().__init__(account_number, balance, customer)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Overdraft limit exceeded.")

# class FixedDeposit(Account):
#     def __init__(self, account_number, balance, customer, interest_rate, maturity_date):
#         super().__init__(account_number, balance, customer)
#         self.interest_rate = interest_rate
#         self.maturity_date = maturity_date

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest earned on fixed deposit: {interest}")
#         return interest




# class Transaction:
#     def __init__(self, transaction_id, account, amount):
#         self.transaction_id = transaction_id
#         self.account = account
#         self.amount = amount

# class Deposit(Transaction):
#     def process_transaction(self):
#         self.account.deposit(self.amount)

# class Withdrawal(Transaction):
#     def process_transaction(self):
#         self.account.withdraw(self.amount)

# class Transfer(Transaction):
#     def __init__(self, transaction_id, from_account, to_account, amount):
#         super().__init__(transaction_id, from_account, amount)
#         self.to_account = to_account

#     def process_transaction(self):
#         if self.amount <= self.account.balance:
#             self.account.withdraw(self.amount)
#             self.to_account.deposit(self.amount)
#             print(f"Transferred: {self.amount} from {self.account.account_number} to {self.to_account.account_number}.")
#         else:
#             print("Insufficient funds for transfer.")



# def main():
#     accounts = {}
#     transaction_id = 1
    
#     while True:
#         print("\n1. Create Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Transfer Money")
#         print("5. Calculate Interest")
#         print("6. Exit")
        
#         choice = input("Choose an option: ")
        
#         if choice == '1':
#             acc_type = input("Enter account type (savings/checking/fixed): ")
#             account_number = input("Enter account number: ")
#             balance = float(input("Enter initial balance: "))
#             customer = input("Enter customer name: ")
            
#             if acc_type == 'savings':
#                 interest_rate = float(input("Enter interest rate: "))
#                 accounts[account_number] = SavingsAccount(account_number, balance, customer, interest_rate)
#             elif acc_type == 'checking':
#                 overdraft_limit = float(input("Enter overdraft limit: "))
#                 accounts[account_number] = CheckingAccount(account_number, balance, customer, overdraft_limit)
#             elif acc_type == 'fixed':
#                 interest_rate = float(input("Enter interest rate: "))
#                 maturity_date = input("Enter maturity date (YYYY-MM-DD): ")
#                 accounts[account_number] = FixedDeposit(account_number, balance, customer, interest_rate, maturity_date)
#             else:
#                 print("Invalid account type.")

#         elif choice == '2':
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter amount to deposit: "))
#             if account_number in accounts:
#                 Deposit(transaction_id, accounts[account_number], amount).process_transaction()
#             else:
#                 print("Account not found.")

#         elif choice == '3':
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter amount to withdraw: "))
#             if account_number in accounts:
#                 Withdrawal(transaction_id, accounts[account_number], amount).process_transaction()
#             else:
#                 print("Account not found.")

#         elif choice == '4':
#             from_account_number = input("Enter your account number: ")
#             to_account_number = input("Enter beneficiary account number: ")
#             amount = float(input("Enter amount to transfer: "))
#             if from_account_number in accounts and to_account_number in accounts:
#                 Transfer(transaction_id, accounts[from_account_number], accounts[to_account_number], amount).process_transaction()
#             else:
#                 print("One or both accounts not found.")

#         elif choice == '5':
#             account_number = input("Enter account number: ")
#             if account_number in accounts:
#                 if isinstance(accounts[account_number], SavingsAccount):
#                     accounts[account_number].calculate_interest()
#                 elif isinstance(accounts[account_number], FixedDeposit):
#                     accounts[account_number].calculate_interest()
#                 else:
#                     print("Interest calculation not applicable for this account type.")
#             else:
#                 print("Account not found.")

#         elif choice == '6':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid option. Please try again.")

# if __name__ == "__main__":
#     main()