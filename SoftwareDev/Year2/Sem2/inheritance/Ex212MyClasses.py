class Account:

    def __init__(self,  balance):
        self._balance = balance

    def getBalance(self):
        return self._balance

    def withdraw(self, amt):
        if (amt <= self._balance):
            self._balance -= amt
            return True
        else:
            return False

    # Extended Class
class DepositAccount(Account):
    def __init__(self, name, val1):
        super().__init__(val1)
        self.__name = name

    def getName(self):
        return self.__name

    def deposit(self, amt):
        self._balance += amt
