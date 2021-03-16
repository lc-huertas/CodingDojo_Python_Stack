class User:  # declare a class and give it name User
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} deposited ${amount}")
        return self
    def withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.name} withdrew ${amount}")
        return self
    def balance(self):
        print(f"{self.name} -> balance: ${self.account_balance}")
        return self

    def transfer(self, recipient, amount):
        if (self.account_balance - amount < 0):
            print("Insufficient funds: cannot execute transfer.")
        else:
            self.withdrawal(amount)
            recipient.deposit(amount)
            print(f"{self.name} transferred ${amount} to {recipient.name}")
        return self


My = User("Luis Huertas", "lhuertas92@gmail.com")
print(My.email)

My.deposit(50).withdrawal(5).balance()

President = User("Joe Biden", "sleepyjoe46@aol.com")
President.deposit(1e5).transfer(My, 1400)