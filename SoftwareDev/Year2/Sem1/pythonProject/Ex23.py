def main():
    val1 = int(input("Enter Value 1: "))
    val2 = int(input("Enter Value 2: "))

    print("Enter option 1 to Add")
    print("Enter option 2 to Multiply")
    print("Enter option 3 to Subtract")

    choice = int(input("Enter option choice: "))
    if choice == 1:
        add = val1+val2
        print("Sum of {0}, {1} is {2}".format(val1, val2, add))
    elif choice == 2:
        mult = val1*val2
        print("Mult of {0}, {1} is {2}".format(val1, val2, mult))
    else:
        subtracted = val1-val2
        print("Subtraction of {0}, {1} is {2}".format(val1, val2, subtracted))



main()