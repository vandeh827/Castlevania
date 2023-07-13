class CurrentBankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


# Example usage:
account = CurrentBankAccount("1234567890", "John Doe", 1000)

print(f"Account Holder: {account.account_holder}")
print(f"Account Number: {account.account_number}")
print(f"Current Balance: {account.get_balance()}")

account.deposit(500)
print(f"Updated Balance after deposit: {account.get_balance()}")

account.withdraw(200)
print(f"Updated Balance after withdrawal: {account.get_balance()}")
