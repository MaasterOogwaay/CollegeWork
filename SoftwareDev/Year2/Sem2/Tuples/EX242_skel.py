
def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4, 5}

    result = countBoth(set1, set2)
    print('# Unique Elements found in both sets = {0}'.format(result))


def countBoth(setp1, setp2):
    result = 0
    union = setp1.intersection(setp2)
    result = len(union)

    return result


main()
