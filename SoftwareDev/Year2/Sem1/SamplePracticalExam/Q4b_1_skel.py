def main():
    list1 = [29, 5, 22, 88, 7, 3, 378, 5]
    result = addDoubleDigit(list1)
    print('Sum of Double Digit elements in list = {0}'.format(result))


def addDoubleDigit(listp):
    if len(listp) == 0:
        return 0
    else:
        total = 0
        first = listp.pop(0)
        if 10 <= first < 100:
            total += first
            return first + addDoubleDigit(listp)
        else:
            return 0 + addDoubleDigit(listp)


main()
