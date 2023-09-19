def main():
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    even_count = 0
    for value in range(lower_limit, upper_limit + 1):
        if (value % 2) == 0:
            print(value)
            even_count += 1
    print("There are {0} even numbers".format(even_count))


main()
