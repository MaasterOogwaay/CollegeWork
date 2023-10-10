class IndexTooHigh(Exception):
    pass


class IndexTooLow(Exception):
    pass


def readValue(list, index):
    # raise goes here
    if index >= len(list):
        raise IndexTooHigh
    elif index < 0:
        raise IndexTooLow
    else:
        value1 = list[index]
        return value1


def main():
    index = int(input("Enter Index:"))
    list = [1, 4, 5, 6, 4]
    # try goes here
    try:
        result1 = readValue(list, index)
        print('Result1= {0}'.format(result1))
    # except goes here
    except IndexTooHigh:
        print("Index too high")
    except IndexTooLow:
        print("Index is negative")


main()
