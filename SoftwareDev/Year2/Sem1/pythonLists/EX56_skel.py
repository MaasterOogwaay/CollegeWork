def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    result = allInRange(list1, lower, upper)
    print("{0} = All elements between {1} and {2} inclusive".format(result, lower, upper))


def allInRange(listp, low, high):
    result = True
    for num in listp:
        if num <= low or num >= high:
            result = False
    return result


main()
