def main():
    value=int(input('Enter an Integer Value (0 to stop): '))
    total=0
    while value != 0:
        if value % 2 != 0:
            total += value
        value = int(input('Enter an Integer Value (0 to stop): '))
    print("Sum of Odd Items = {0}".format(total))

main()

