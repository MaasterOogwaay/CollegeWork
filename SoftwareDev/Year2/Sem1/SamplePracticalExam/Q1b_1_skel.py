
def main():
    height = int(input('Enter Height: '))
    symbol = input('Enter Symbol: ')
    displayDiagonalLine(symbol, height)


def displayDiagonalLine(symbol, height):
    for i in range(height):
        print(' ' * i, end='{0}\n'.format(symbol))


main()

