import sys


def fun1():
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)
    v1 = int(sys.argv[1])
    v2 = int(sys.argv[2])
    result = sum(v1,v2)
    print("\nSum of {0},{1} = {2}".format(v1, v2, result))


def sum(value1, value2):
    return value1 + value2


fun1()
