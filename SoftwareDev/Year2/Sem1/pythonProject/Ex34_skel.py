def main():
    base = int(input('Enter Base: '))
    pow = int(input('Enter Power: '))
    result = power(base, pow)
    print('{0} to Power of {1}= {2}'.format(base, pow, result))


def power(base, pow):
    result = 1
    for values in range(1, pow + 1):
        result = result * base
    return result


main()
