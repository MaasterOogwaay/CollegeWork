
class Money:
    def __init__(self, e, c):
        self.euro = e 
        self.cent = c

    def printMoney(self):
        print('€{0}.{1}'.format(self.euro, self.cent))

    def __iadd__(self, other):
        result = Money(self.euro + other.euro, self.cent + other.cent)
        if result.cent > 99:
            result.euro += 1
            result.cent -= 100
        return result

    def __sub__(self, other):
        total1 = (self.euro * 100) + self.cent
        total2 = (other.euro * 100) + other.cent
        res = total1 - total2
        euro_res = int(res / 100)
        cent_res = int(res % 100)
        return Money(euro_res, cent_res)


def main():
    m1 = Money(2, 43)
    m2 = Money(5, 29)
    m3 = Money(9, 73)
    res1 = m2 - m1
    print('\n(5.29 - 2.43= ', end='')
    res1.printMoney()

    res2 = m3 - m2
    print('\n (9.73 - 5.29= ', end='')
    res2.printMoney()
    
    m3 += m1
    print('\n (9.73 += 2.43= ', end='')
    m3.printMoney()


main()
