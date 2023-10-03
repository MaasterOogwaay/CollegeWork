def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    result = addInRange(list1, lower, upper)
    print("{0} = sum of elements between {1} and {2}".format(result, lower, upper))

def addInRange(listp, low, high):
    result = 0
    for num in listp:
        if (num >= low and num <= high):
            result = result + num
    return result


main()
