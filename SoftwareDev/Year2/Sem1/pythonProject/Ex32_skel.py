def main():
    val1 = int(input("Enter Value: "))
    result = sigma(val1)
    print("Sigma {0} = {1}".format(val1, result))


def sigma(val1):
    result = 0
    for value in range(1, val1 + 1):
        result = result + value
    return result


main()
