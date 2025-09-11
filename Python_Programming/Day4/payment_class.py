class Payment:
    def __init__(self):
        pass
    def pay():
        pass

class CashPayment(Payment):
    def __init__(self):
        pass
    def pay(self, amount):
        print(f"Paid {amount} in cash")

class CardPayment(Payment):
    def __init__(self):
        pass
    def pay(self, amount):
        print(f"Paid {amount} using credit/debit card")

class UPIPayment(Payment):
    def __init__(self):
        pass
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

list = [CardPayment(), CashPayment(), UPIPayment()]
for i in list:
    i.pay(1000)