def countOddElements(listp):
    if len(listp) == 0:
        return 0
    else:
        count = 0
        first = listp.pop(0)
        if first % 2 == 1:
            count += 1
            return 1 + countOddElements(listp)
        else:
            return 0 + countOddElements(listp)


def main():
    list = [2, 3, 4, 5, 6, 7, 9]
    result = countOddElements(list)
    print('{0} odd elements in the list [2,3,4,5,6,7,9]'.format(result))


main()

