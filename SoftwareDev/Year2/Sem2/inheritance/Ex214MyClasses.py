class Stepper:

    def __init__(self, val):
        self._value = val

    def stepDown(self, amount):
        if amount <= self._value:
            self._value -= amount
            return True
        else:
            return False

    def getValue(self):
        return self._value

# Extended Class


class MyStepper(Stepper):
    def __init__(self, val1, limit):
        super().__init__(val1)
        self.__limit = limit

    def stepUp(self, amt):
        if (self._value + amt) > self.__limit:
            return False
        else:
            self._value += amt
            return True

    def getLimit(self):
        return self.__limit

    def resetLimit(self, amt):
        self.__limit = amt
