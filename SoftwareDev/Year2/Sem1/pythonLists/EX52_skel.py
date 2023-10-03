def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = addOdd(list1)
    print('Sum of Odd els in list = {0}'.format(result))


def addOdd(listp):
    result = 0
    for num in listp:
        if num % 2 == 1:
            result = result + num
    return result


main()
