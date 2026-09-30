class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New Balance =", self.balance)

acc = BankAccount("Sujan", 10000)

acc.deposit(10000)
acc.deposit(1100)
