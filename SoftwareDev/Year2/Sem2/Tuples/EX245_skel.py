
def main():
    studentList = {'Smith': 58, 'Jones': 86, 'peters': 78, 'Adams': 44, 'Cross': 25}
    lower = int(input('Enter Lower Age: '))
    upper = int(input('Enter Upper Age: '))
    printInRange(studentList, lower, upper)


def printInRange(studentL, low, high):
    print("\nList of Names")
    print("================")
    for key, value in studentL.items():
        if low <= value <= high:
            print(key)


main()
