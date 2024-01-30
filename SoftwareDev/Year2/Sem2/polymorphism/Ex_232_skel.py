
class Operation:
    def __init__(self, val1):
        self._value1 = val1

    def op(self):
        return 0

    def readType(self):
        return 'Base Operation'

    def printData(self):
        print(self.readType())
        print('Initial Value= ', self._value1)


class Increment(Operation):
    def __init__(self, val):
        super().__init__(val)

    def readType(self):
        return 'Increment'

    def op(self):
        return self._value1 + 1


class Decrement(Operation):
    def __init__(self, val):
        super().__init__(val)

    def readType(self):
        return 'Decrement'

    def op(self):
        return self._value1 - 1


class Double(Operation):
    def __init__(self, val):
        super().__init__(val)

    def readType(self):
        return 'Double'

    def op(self):
        return self._value1 * 2

def main():
    obj1=Increment(1)
    obj2=Decrement(4)
    obj3=Double(6)
    list = [obj1, obj2, obj3]
    for el in list:
        print('---------')
        el.printData()
        print('Result = ', el.op())

main()

