def main():
    list1 = [2, 5, 2, 28, 7, 23, 2, 45]
    target = int(input('Enter Target: '))
    result = countGreater(list1, target)
    print('{0} Occurs in List {1} Times'.format(target, result))


def countGreater(list, target):
    count = 0
    for el in list:
       if el > target:
          count += 1
    return count


main()
