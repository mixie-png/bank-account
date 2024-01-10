class BankAccount:
    # class attribute - a list of all the accounts!
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            print(sum)
        return sum

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount < self.balance:
            self.balance -= amount
        else:
            self.balance -= amount + 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self


# user accounts
account1 = BankAccount(0.05, 2500)
account2 = BankAccount(0.1, 1000000)

account1.deposit(50).deposit(150).deposit(200).withdraw(100).yield_interest().display_account_info()
account2.deposit(1000).deposit(10000).withdraw(500000).withdraw(250000).withdraw(250000).withdraw(125000).yield_interest().display_account_info()

BankAccount.all_balances()