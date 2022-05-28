class BankAccount:
    all_accounts_info = []
    def __init__(self, name= "None", int_rate = .05, balance = 0): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts_info.append(self)
        
#Instance Menthods:
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"{self.name}, your balance is: ${self.balance}, and your current interest rate is: {self.int_rate:.0%}.")
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    def print_accounts(self):
        print(f"info for {self.name} = Balance: ${self.balance}, interest rate: {self.int_rate:.0%}")

#Class Method(s):
    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.all_accounts_info:
            accounts.print_accounts()

jack = BankAccount(name="jack", balance= 100)
jack.display_account_info()
aaron = BankAccount(name="aaron", balance= 200)
aaron.display_account_info()
jack.deposit(20).deposit(60).yield_interest().display_account_info()
aaron.deposit(20).deposit(30).withdraw(50).withdraw(10).withdraw(20).withdraw(50).yield_interest().display_account_info()
BankAccount.print_all_accounts()