class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds")


class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self.withdraw_limit = 100   # Step 1: set withdraw limit

    # Step 2: override withdraw method
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied! Limit is ${self.withdraw_limit}")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
