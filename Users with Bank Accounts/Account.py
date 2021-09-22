
class BankAccount:
    bank = "CodingBank"
    accounts = []

    def __init__(self, int_rate, balance): 
        
        self.balance = balance
        self.interest = int_rate
        BankAccount.accounts.append( self )


    
    def deposit(self, amount):
        self.balance += amount
        print (f"You have deposited ${amount}")
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You dont have enough money")
            print( f"You current balance is ${self.balance}")
            print( f"But you are trying to withdraw ${amount}")
            self.balance -= 5
        return self


    def display_account_info(self):
        print( f"You current balance is ${self.balance}")
        return self
    
    def yield_interest(self):
        
        if self.balance > 1:
            interestsamount = self.balance * (self.interest / 100)
            self.balance += interestsamount
        return self



#=========================================================================
    def printInformation(self):
        print( f"Account Balance {self.balance}")
        print( f"The interest added to you account are %{self.interest}")

    @classmethod
    def printAllAccountsInfo(cls):
        print(f"This is the information of the the accounts")
        for account in cls.accounts:
            account.printInformation()


