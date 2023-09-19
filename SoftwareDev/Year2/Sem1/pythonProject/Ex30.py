def main():
    value = int(input("Enter a Value 1-9 (0 to stop): "))
    maximum = value
    while value != 0:
        if value > maximum:
            maximum = value
        value = int(input("Enter a Value 1-9 (0 to stop): "))
    print("Max number is = {0}".format(maximum))


main()
