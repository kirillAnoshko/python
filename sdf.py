class ATM:
    def __init__(self):
        self.id = 0
        self._total = 0

    def Deposit(self, money):
        self.total += money
        print(f"Внесли {money}, на счёте {self.total}")

    def withdraw(self, money):
        print("карта опознана")
        print("пин-код принят")
        self.total -= money
        print(f"Сняли {money}, на счёте {self.total}")

atm = ATM()

atm.total -= 1000000
print(atm.total)
