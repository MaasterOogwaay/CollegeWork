def main():
    list1 = [22, 5, 6, 8, 7]
    next1 = int(input('Enter next Item: '))
    list1.append(next1)
    next2 = int(input('Enter next Item: '))
    list1.append(next2)

    result = myMinimum(list1)
    print('Minimum Item = {0}'.format(result))


def myMinimum(listp):
    result = listp[0]
    for i in listp:
        if i < result:
            result = i
    return result


main()