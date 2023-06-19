from tkinter import *
from tkinter import messagebox
class BankApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank App")
        self.balance = 10000

        # Create labels, entry fields, and buttons
        self.balance_label = Label(self, text="Balance:")
        self.balance_label.pack()

        self.balance_entry = Entry(self)
        self.balance_entry.insert(0, f"{self.balance}")
        self.balance_entry.pack()

        self.deposit_label = Label(self, text="Deposit:")
        self.deposit_label.pack()

        self.deposit_entry = Entry(self)
        self.deposit_entry.pack()

        self.withdraw_label = Label(self, text="Withdraw:")
        self.withdraw_label.pack()

        self.withdraw_entry = Entry(self)
        self.withdraw_entry.pack()

        self.balance_button = Button(self, text="Check Balance", command=self.check_balance, bg='green')
        self.balance_button.pack()

        self.deposit_button = Button(self, text="Deposit", command=self.deposit, bg='grey')
        self.deposit_button.pack()

        self.withdraw_button = Button(self, text="Withdraw", command=self.withdraw, bg='red')
        self.withdraw_button.pack()

    def check_balance(self):
        # Retrieve balance from the entry field and display it
        balance = self.balance_entry.get()
        self.show_message("Your balance is $" + balance)

    def deposit(self):
        # Retrieve deposit amount from the entry field, add it to the balance, and display the updated balance
        deposit_amount = self.deposit_entry.get()
        self.balance += float(deposit_amount) 
        self.show_message("Deposit successful. Your new balance is $" + str(self.balance))
        self.balance_entry.delete(0, END)
        self.balance_entry.insert(0, f"{self.balance}")

    def withdraw(self):
        # Retrieve withdrawal amount from the entry field, subtract it from the balance, and display the updated balance
        withdraw_amount = self.withdraw_entry.get()
        balance = self.balance_entry.get()

        if float(balance) >= float(withdraw_amount):
            self.balance = float(balance) - float(withdraw_amount)
            self.show_message("Withdrawal successful. Your new balance is $" + str(self.balance))
        else:
            self.show_message("Insufficient funds.")

    def show_message(self, message):
        # Create a message box to display information or notifications
        self.balance_entry.delete(0, END)
        self.balance_entry.insert(0, f"{self.balance}")
        messagebox.showinfo("Bank App", message)

# Create an instance of the BankApp class and run the application
if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
