def main():
    print("Price =£", end="")
    printPrice(2.34)
    print("\nPrice in Dollars=", end="")
    dollar_decorator(printPrice)(round(2.34*1.13, 2))
    print("\nPrice in Euro=", end="")
    euro_decorator(printPrice)(round(2.34*1.15, 2))


def dollar_decorator(func):
    def inner(price):
        print("$", end="")
        func(price)
    return inner


def euro_decorator(func):
    def inner(price):
        print("€", end="")
        func(price)
    return inner


def printPrice(price):
    print(price)


main()
