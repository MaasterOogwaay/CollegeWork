
def main():
    first = int(input('Enter start: '))
    last = int(input('Enter End: '))
    result = addBetween(first, last)
    print('Sum of values between {0} and {1} = {2}'.format(first,last, result))


def addBetween(start, end):
    sumOfValues = 0
    for value in range(start, end + 1):
        sumOfValues += value
    return sumOfValues


main()

