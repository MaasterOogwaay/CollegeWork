from enum import IntEnum


class ChooseFunction(IntEnum):
    Increment = 1
    Decrement = 2


def main():
    x = int(input('Enter Initial Value: '))
    print('\nOptions')
    print('---------')
    print('Enter {0} for Increment'.format(ChooseFunction.Increment))
    print('Enter {0} for Decrement'.format(ChooseFunction.Decrement))
    choice = int(input('Enter Choice:'))
    if choice == ChooseFunction.Increment:
        print("\nres=", (x+1))
    elif choice == ChooseFunction.Decrement:
        print("\nres=", (x-1))


main()
