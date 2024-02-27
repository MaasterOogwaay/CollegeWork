
class Height:
    def __init__(self, f, i):
        self.feet = f 
        self.inches = i

    def printHeight(self):
        print('{0}\'-{1}\"'.format(self.feet, self.inches))

    def __add__(self, other):
        result = Height(self.feet + other.feet, self.inches + other.inches)
        if result.inches > 11:
            result.feet += 1
            result.inches -= 12
        return result

    def __isub__(self, other):
        total1 = (self.feet * 12) + self.inches
        total2 = (other.feet * 12) + other.inches
        res = total1 - total2
        feet_res = int(res / 12)
        inches_res = int(res % 12)
        return Height(feet_res, inches_res)

    def __eq__(self, other):
        if self.feet == other.feet and self.inches == other.inches:
            return True
        else:
            return False


def main():
    h1 = Height(5, 10)
    h2 = Height(5, 10)
    h3 = Height(8, 5)
    res1 = h1 + h3
    print('\n5 ft 10 ins + 8 ft 5 ins= ', end='')
    res1.printHeight()

    h3 -= h2
    print('\n 8 ft 1 ins -= 5 ft 9 ins= ', end='')
    h3.printHeight()
    
    if h1 == h2:
        print('\nBoth 5 ft 10 ins')
        
    if h1 == h3:
        print('\nBoth are not 5 ft 10 ins')


main()
