

def main():
    value = int(input('Enter Value 1-99 (negative number to stop):'))
    total = 0

    while value > 0:
        if value >= 1 and value < 10:
            total += value
        value = int(input('Enter Value 1-99 (negative number to stop):'))

    print('Sum of Single Digit Elements = {0}'.format(total))


main()
