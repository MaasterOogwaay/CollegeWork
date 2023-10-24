

def main():
    value = int(input('Enter Value 1-100 (0 to stop):'))
    total = 0
    # to be completed with while loop
    while value != 0:
        if value % 2 == 0:
            total += value
        value = int(input('Enter Value 1-100 (0 to stop):'))

    print('Sum of Even Elements = {0}'.format(total))


main()
