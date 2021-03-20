class BankAccount:
    def __init__(self, account_name, int_rate, balance):
        self.name = account_name
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.name}-account balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 + self.interest)
        return self


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.Accounts = []

    def Create_Account(self, acc_name, int_rate, balance):
        self.Accounts.append(BankAccount(acc_name, int_rate, balance))
        return self
    def Get_Account(self,acc_name):
        for i in range(0,len(self.Accounts)):
            if(acc_name==self.Accounts[i].name):
                return self.Accounts[i]



Luis=User('Luis','luis10@gmail.usf.edu')
Luis.Create_Account('Checkings',0.05,2000)
Luis.Create_Account('Savings',0.01,900)

Luis.Get_Account('Checkings').display_account_info()
Luis.Get_Account('Checkings').deposit(700)
Luis.Get_Account('Checkings').display_account_info()

