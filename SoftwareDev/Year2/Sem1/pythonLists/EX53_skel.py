def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    target = int(input("Enter Target: "))
    result = countTarget(list1, target)
    print("{0} occurs in list {1} times".format(target, result))


def countTarget(listp, tar):
    result = 0
    for num in listp:
        if num == tar:
            result = result + 1
    return result


main()
