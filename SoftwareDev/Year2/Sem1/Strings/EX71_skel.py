

def main():
    word = 'ballinasloe'
    target = str(input('Enter Target Letter: '))
    result = countLetter(word, target[0])
    print('{0} Occurs in List {1} Times'.format(target[0], result))


def countLetter(word, tar):
    result = 0
    for el in word:
        if el == tar:
            result += 1
    return result


main()
