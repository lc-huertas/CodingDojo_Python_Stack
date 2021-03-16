class BankAccount:
    def __init__(self, int_rate, balance):  # don't forget to add some default values for these parameters!
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon.
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self
    def display_account_info(self):
        # your code here
        print(f"Account balance: ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance * (1 + self.interest)
        return self

# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class  Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals,
# then calculate interest and display the account's info all in one line of code (i.e. chaining)

Acc1 = BankAccount(0.01,100)
Acc2 = BankAccount(0.03,50)

Acc1.deposit(5).deposit(5).deposit(5).withdraw(5).yield_interest().display_account_info()
Acc1.deposit(5).deposit(5).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()