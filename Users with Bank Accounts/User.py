from Account import BankAccount


class User:

    accounts = []

    def __init__(self, accountOwner, accountNumber):
        self.Owner = accountOwner
        self.accNumber = accountNumber
        self.balance = BankAccount(int_rate=3, balance=0)
        User.accounts.append(self)


    def withdraw(self, amount):
        if amount <= self.balance.balance:
            self.balance.withdraw(amount)
        else:
            print("You dont have enough money")
            print( f"You current balance is ${self.balance.balance}")
            print( f"But you are trying to withdraw ${amount}")
            print("We are going to charge you $5")
            self.balance.balance -= 5
        return self
        

    def deposit(self, amount):
        self.balance.deposit(amount)
        return self

    def display_user_info(self):
        print(f"User: {self.Owner}, Account Balance ${self.balance.balance}")
        return self

    def transfer_money(self,amount,other_user):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

