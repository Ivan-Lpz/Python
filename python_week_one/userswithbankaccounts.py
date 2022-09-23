class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name   
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        self.rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount 


bob = User("Bob", "Charles", "bobcharles@yahoo.com", 30) 
anthony = User("anthony", "godman", "godman@yahoo.com", 23)
aman = User("aman", "demonman", "demonman@yahoo.com", 22) 

bob.enroll()
anthony.enroll()
anthony.spend_points(80)
bob.spend_points(50)
bob.display_info()
anthony.display_info()
aman.display_info()

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
account2.display_account_info().deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(5).withdraw(5)