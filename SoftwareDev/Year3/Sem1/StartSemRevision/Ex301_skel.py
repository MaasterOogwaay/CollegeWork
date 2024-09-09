

def main():
    val1 =  int(input('Enter Value: '))
    val2 =  int(input('Enter Value: '))
    val3 = int(input('Enter Value: '))
    result = my_max(val1, val2, val3)
    print('Max= {0}'.format(result))


def my_max(val1, val2, val3):
    if val2 < val1 > val3:
        return val1
    if val1 < val2 > val3:
        return val2
    if val1 < val3 > val2:
        return val3


main()
