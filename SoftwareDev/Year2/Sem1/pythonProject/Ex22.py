def main():
    val1 = int(input("Enter Value 1: "))
    val2 = int(input("Enter Value 2: "))
    val3 = int(input("Enter Value 3: "))

    if (val1 > val2) and (val1 > val3):
        print("{0} is largest".format(val1))
    elif (val2 > val1) and (val2 > val3):
        print("{0} is largest".format(val2))
    else:
        print("{0} is largest".format(val3))


main()