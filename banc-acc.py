class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self  # Return self for chaining

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5  # Charge a $5 fee
            print("Insufficient funds: Charging a $5 fee")
        return self  # Return self for chaining

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self  # Return self for chaining

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self  # Return self for chaining

    @classmethod
    def print_all_accounts(cls, accounts):
        for account in accounts:
          account.display_account_info()

# Create 2 accounts
account1 = BankAccount()  # Default interest rate and balance
account2 = BankAccount(int_rate=0.02, balance=100)  # Custom interest rate and balance

# Chaining method calls for account1
account1.deposit(100).deposit(50).deposit(200).withdraw(75).yield_interest().display_account_info()

# Chaining method calls for account2
account2.deposit(200).deposit(150).withdraw(50).withdraw(75).withdraw(100).withdraw(200).yield_interest().display_account_info()

# NINJA BONUS: Print all account info using classmethod
accounts = [account1, account2]
BankAccount.print_all_accounts(accounts)