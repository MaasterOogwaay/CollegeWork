def main():
    checkEqualZero = my_checkEqual(0)
    checkEqualOne = my_checkEqual(1)
    checkEqualTen = my_checkEqual(10)

    res = checkEqualZero(0)
    print(res)
    res = checkEqualZero(5)
    print(res)
    res = checkEqualOne(1)
    print(res)
    res = checkEqualTen(5)
    print(res)


def my_checkEqual(value1):
    def f2(value2):
        return value1 == value2
    return f2


main()
