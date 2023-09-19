

def main():
    val1 = int(input('Enter Value: '))
    val2 = int(input('Enter Value: '))
    result = my_max(val1, val2)
    print('Max= {0}'.format(result))


def my_max(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2


main()
