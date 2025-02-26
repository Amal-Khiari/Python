class BankAccount:
    # ... (BankAccount class remains the same)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def create_account(self, account_name, int_rate=0.02, balance=0):
        if account_name in self.accounts:
            print(f"Account '{account_name}' already exists for {self.name}.")
            return self  # Return self for chaining

        self.accounts[account_name] = BankAccount(int_rate, balance)
        print(f"Account '{account_name}' created for {self.name}.")
        return self

    def make_deposit(self, amount, account_name):
        account = self.get_account(account_name)
        if account:
            account.deposit(amount)
            print(f"Deposited ${amount} into {self.name}'s '{account_name}' account.")
        return self

    def make_withdrawal(self, amount, account_name):
        account = self.get_account(account_name)
        if account:
            account.withdraw(amount)
            print(f"Withdrew ${amount} from {self.name}'s '{account_name}' account.")
        return self

    def display_user_balance(self, account_name=None):
        if account_name:
            account = self.get_account(account_name)
            if account:
                print(f"User: {self.name}, Account: {account_name}, Balance: ${account.balance}")
        else:
            print(f"User: {self.name}")
            for account_name, account in self.accounts.items():
                print(f"Account: {account_name}, Balance: ${account.balance}")
        return self

    def transfer_money(self, amount, other_user, from_account_name, to_account_name):
        from_account = self.get_account(from_account_name)
        to_account = other_user.get_account(to_account_name)

        if from_account and to_account:
            if from_account.balance >= amount: # Check for sufficient funds *before* withdrawing
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount} from {self.name}'s '{from_account_name}' to {other_user.name}'s '{to_account_name}'")
            else:
                print(f"Insufficient funds in {self.name}'s '{from_account_name}' account for the transfer.")
        return self

    # Helper function to get an account object or print an error
    def get_account(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name]
        else:
            print(f"Account '{account_name}' not found for {self.name}.")
            return None