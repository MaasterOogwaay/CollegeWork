
class Line:
    def __init__(self, length):
        self._length = length

    def draw(self):
        print('Base Class')


class VertLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
       print()
       for i in range(self._length):
           print(' *')


class HorzLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print()
        for i in range(self._length):
            print('*', end=' ')


class SlashLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print()
        for i in range(self._length):
            print(' '*i, end='*\n')


class Square(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        # for j in range(self._length):
        #     print()
        #     for i in range(self._length):
        #         print('*', end=' ')
        for i in range(self._length):
            print('* '*self._length, end='\n')






def main():
    obj1 = VertLine(5)

    # obj2=VertLine(6)
    obj2 = HorzLine(6)

    # obj3 = VertLine(7)
    obj3 = SlashLine(7)

    # obj4 = VertLine(8)
    obj4 = Square(8)

    list = [obj1, obj2, obj3, obj4]
    for el in list:
        print('')
        el.draw()


main()

