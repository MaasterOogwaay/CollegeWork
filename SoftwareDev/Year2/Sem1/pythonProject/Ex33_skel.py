def main():
    val1 = int(input('Enter Value: '))
    result = factorial(val1)
    print('Factorial {0}= {1}'.format(val1, result))


def factorial(val1):
    result = 1
    for value in range(1, val1 + 1):
        result = result * value
    return result


main()
