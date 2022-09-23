class BankAccount:
    def __init__(self,balance,interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self,amount):
        self.balance += amount
        return self

    

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.interest_rate)
        return self

    def yield_interest(self):
        self.balance = self.balance * self.interest_rate + self.balance

account1 = BankAccount(100,.05)
account2 = BankAccount(50,.05)

account1.display_account_info().deposit(5).deposit(5).deposit(5).withdraw(20).display_account_info()
account2.display_account_info().deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(5).withdraw(5).display_account_info()
#account1.yield_interest()
#account1.display_account_info()





    


                                                            # don't forget to add some default values for these parameters!
                                                            # def __init__(self, int_rate, balance): 
                                                            #     # your code here! (remember, instance attributes go here)
                                                            #     # don't worry about user info here; we'll involve the User class soon
                                                            # def deposit(self, amount):
                                                            #     # your code here
                                                            # def withdraw(self, amount):
                                                            #     # your code here
                                                            # def display_account_info(self):
                                                            #     # your code here
                                                            # def yield_interest(self):
                                                            #     # your code here
