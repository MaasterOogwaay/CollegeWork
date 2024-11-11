def main():
    value = input('Enter Name ')
    print()
    printName(value)
    print()
    printHello(value)


def trace_decorator(func):
    def closure(value):
        print(func.__name__)
        func(value)

    return closure


@trace_decorator
def printName(value):
    print("\nName is: ", value)


@trace_decorator
def printHello(value):
    print("\nHello ", value)


main()
