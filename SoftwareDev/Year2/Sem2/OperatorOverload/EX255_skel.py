
class Weight:
    def __init__(self, s, p):
        self.__stone = s
        self.__pound = p

    def printTime(self):
        print('{0}-st : {1}-lb'.format(self.__stone, self.__pound))
            
    def __iadd__(self, other):
        result = Weight(self.__stone + other.__stone, self.__pound + other.__pound)
        if result.__pound > 13:
            result.__stone += 1
            result.__pound -= 14
        return result

    def __ge__(self, other):
        total1 = ((self.__stone * 14) + self.__pound)
        total2 = ((other.__stone * 14) + other.__pound)
        if total1 >= total2:
            return True
        else:
            return False


def main():
    w1 = Weight(8, 6)
    w2 = Weight(5, 13)
    w1 += w2
    print('\n( 8 st - 6 lb    +   (5 st - 13 lb ) = ', end='')
    w1.printTime()

    if w1 >= w2:
        print('\n(8 st - 6 lb)  >= (5 st - 13 lb)')
    else:
        print('\n(8 st - 6 lb)  NOT >= (5 st - 13 lb)')

    if w2 >= w1:
        print('\n(5 st - 13 lb) >= (8 st - 6 lb)')
    else:
        print('\n(5 st - 13 lb) NOT >= (8 st - 6 lb)')

    if w1 >= w1:
        print('\n(8 st - 6 lb)  >= (8 st - 6 lb)')


main()
