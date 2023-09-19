def main():
    value = int(input("Enter a Value 1-9 (0 to stop): "))
    total = 0
    while value != 0:
        total = total + value
        value = int(input("Enter a Value 1-9 (0 to stop): "))
    print("Sum = {0}".format(total))


main()
