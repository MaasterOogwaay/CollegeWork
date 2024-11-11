def main():
    value = input('Enter Name: ' )
    printName(value)


def confirmation_decorator(func):
        def closure(value):
            res = input('Enter Y to confim action: ')
            if res == "Y":
                func(value)
            else:
                print("Action Cancelled")
        return closure


@confirmation_decorator
def printName(value):
    print("Name is: ", value)


main()
