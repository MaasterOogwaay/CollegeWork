def main():
    count = 1
    total = 0
    for value in range(1, 6):
        user_input = int(input("Enter Value {0}: ".format(count)))
        total += user_input
        count += 1
    print("Sum of 5 values = {0}".format(total))


main()
