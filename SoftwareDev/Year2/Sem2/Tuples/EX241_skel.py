
def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4}
    target = int(input('Enter Target: '))
    result = mySearch(set1, set2, target)
    print('Element {0} found in at least 1 set = {1}'.format(target, result))


def mySearch(setp1, setp2, tar):
    result = False
    if tar in setp1 or tar in setp2:
        result = True
    else:
        result = False
    return result


main()
