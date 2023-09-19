def main():
    initial_value = int(input("Enter Initial Value: "))
    count = 0
    current_value = initial_value
    while count < 6:
        operation = input("Enter Operation (+/-): ")
        amount = int(input("Enter Amount: "))
        count += 1
        if operation == "+":
            current_value = current_value + amount
            print("Value Now: {0}".format(current_value))
        else:
            current_value = current_value - amount
            print("Value Now: {0}".format(current_value))
    print("Final Value = {0}".format(current_value))


main()
