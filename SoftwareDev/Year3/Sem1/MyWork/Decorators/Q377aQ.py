def main():
    value = input('Enter Name: ')
    printName(value)


def repeat_void_decorator(func):
    def closure(value):
        func(value)
        func(value)
    return closure


@repeat_void_decorator
def printName(value):
    print("Name is: ", value)


main()
