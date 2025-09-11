class BankAccount:
    def __init__(self):
        self.b = 1000
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print(amount,"deposited")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount,"withdrawn")
        else:
            print("Insufficient funds")
    def get_balance(self):
        print("Balance:",self.__balance)

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.get_balance()