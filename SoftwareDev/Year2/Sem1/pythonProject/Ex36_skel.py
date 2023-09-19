def main():
    value1 = int(input('Enter Value 1: '))
    value2 = int(input('Enter Value 2: '))
    value3 = int(input('Enter Value 3: '))
    result = largest(value1,value2,value3)
    print('{0} is largest of 3 valued of {1},{2},{3}'.format(result, value1, value2, value3))


def largest(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    else:
        return z


main()
