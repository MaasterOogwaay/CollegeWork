
def main():
    start = int(input('Enter Start Value: '))
    printNextFive(start)


def printNextFive(start):
    print("[", end="")
    for i in range(start+1, start+6):
        print("{0}".format(i), end=" ")
    print("]")


main()