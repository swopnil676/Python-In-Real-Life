# Bank Account Class
class Account():

    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance = ", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 7890564)
acc1.debit(100)
acc1.credit(1000)

acc2 = Account(50000, 678834567)
acc2.debit(100)
acc2.credit(1000)