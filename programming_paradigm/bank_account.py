class BankAccount:
    def __init__(self, initial_balance_parameter = 0):
        self.account_balance = initial_balance_parameter
        pass

    def deposit(self, amount):
        self.account_balance += amount
        pass

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    pass

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")