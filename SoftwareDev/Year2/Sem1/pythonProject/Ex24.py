def main():
    count = 1
    total = 0
    while count < 6:
        value = int(input("Enter a Value {0}: ".format(count)))
        total += value
        count += 1
    print("Sum of 5 values = {0}".format(total))


main()
