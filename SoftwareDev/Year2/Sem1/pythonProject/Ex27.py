def main():
    name = input("Enter a name: ")
    times_to_print = int(input("Enter the number of times to print: "))
    for value in range(1, times_to_print + 1):
        print("Name = {0}".format(name))


main()
