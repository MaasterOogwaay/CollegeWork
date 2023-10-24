

def main():
    value = int(input('Enter Value 1-99 (negative number to stop):'))
    count = 0
    while value > 0:
        if value > 0 and value < 10:
            count += 1
        value = int(input('Enter Value 1-99 (negative number to stop):'))

    print('Number of Single Digit Elements Entered = {0}'.format(count))


main()
