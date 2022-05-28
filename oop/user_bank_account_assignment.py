class User:
    corp_name = "First National Dojo Bank"
    all_accounts_info = []
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}
        #User.all_accounts_info.append(self)
        
    #Instance Mentods
    def create_account(self, accName):
        self.accounts[accName] = BankAccount()
        User.all_accounts_info.append(self)
        return self
    def make_deposite(self,accName,ammt):
        self.accounts[accName].balance += ammt
        print(f"Congratz {self.first_name}! Your new balance is: ${self.accounts[accName].balance}.")
        return self
    
    def make_withdrawl(self,accName,ammt):
        self.accounts[accName].balance -= ammt
        print(f"Thanks for your withdrawl of: ${ammt}, your new balance is: ${self.accounts[accName].balance}.")
        return self

    def display_account_info(self,accName):
        print(f"{self.first_name}, your balance is: ${self.accounts[accName].balance}, and your current interest rate is: {self.accounts[accName].int_rate:.0%}.")

    def print_accounts(self):
        print(f"info for {self.first_name} = Balance: ${self.accounts.balance}, interest rate: {self.accounts.int_rate:.0%}")

    def transfer_money(self,accName,ammt,accName2,user):
        self.accounts[accName].balance -= ammt
        user.accounts[accName].balance += ammt
        print(f"{self.first_name}, you have transfered ${ammt} to {user.first_name}, your new balance is: ${self.accounts[accName].balance}")
        print(f"{user.first_name}'s new balance is: ${user.accounts[accName2].balance}.")
        return self
    
    def yield_interest(self,accName):
        self.accounts[accName].balance += self.accounts[accName].balance*self.accounts[accName].int_rate
        return self
    
    #Class Method(s):
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts_info:
            account.print_accounts()

class BankAccount:
    def __init__(self, int_rate = .05, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

lakk = User("larry", "Baragellie", "LannyB@iamgod.biz")
chris = User("Chris", "Kringle", "ImNotSanta@iamgod.biz")
laura = User("Laura", "Croft", "LauraC@toomRaider.org")
#print(type(lakk.acc))
#print(lakk.accounts.balance)
lakk.create_account("newAcc")
lakk.display_account_info("newAcc")
lakk.create_account("checking").make_deposite("checking",1000).display_account_info("checking")
lakk.create_account("savings").make_deposite("savings",2000).display_account_info("savings")
laura.create_account("checking").make_deposite("checking", 1000).make_withdrawl("checking",750).yield_interest("checking").display_account_info("checking")
laura.create_account("savings").make_deposite("savings",2100).display_account_info("savings")
chris.create_account("checking").make_deposite("checking",1000).transfer_money("checking", 200,"checking", laura)
chris.create_account("savings").make_deposite("savings",500).display_account_info("savings")
User.print_all_accounts()
