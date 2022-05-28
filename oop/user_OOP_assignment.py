class User:
    corp_name = "First National Dojo Bank"
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.acc_balance = 0
    def acc_bal(self):
        print(f"Hello {self.first_name}, your account balance is: ${self.acc_balance}.")
    def make_deposite(self,ammt):
        self.acc_balance += ammt
        print(f"Congratz {self.first_name}! Your new balance is: ${self.acc_balance}.")
        return self.acc_balance
    def make_withdrawl(self,ammt):
        self.acc_balance -= ammt
        print(f"Thanks for your withdrawl of: ${ammt}, your new balance is: ${self.acc_balance}.")
        return self.acc_balance
    def transfer_money(self,ammt,user):
        self.acc_balance -= ammt
        user.acc_balance += ammt
        print(f"{self.first_name}, you have transfered ${ammt} to {user.first_name}, your new balance is: {self.acc_balance}")
        print(f"{user.first_name}'s new balance is: ${user.acc_balance}.")
        return self.acc_balance, user.acc_balance

# User()

lakk = User("larry", "Baragellie", "LannyB@iamgod.biz")
chris = User("Chris", "Kringle", "ImNotSanta@iamgod.biz")
laura = User("Laura", "Croft", "LauraC@toomRaider.org")
lakk.make_deposite(1000)
lakk.make_deposite(250)
lakk.make_deposite(250)
lakk.make_withdrawl(500)
lakk.acc_bal()
chris.make_deposite(200)
chris.make_deposite(100)
chris.make_withdrawl(50)
chris.acc_bal()
laura.make_deposite(100)
laura.make_withdrawl(50)
laura.make_withdrawl(50)
laura.make_withdrawl(20)
laura.acc_bal()
lakk.transfer_money(30, laura)
lakk.acc_bal()
laura.acc_bal()
# lakk.acc_bal()