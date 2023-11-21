def readWord(text, index):
    textList = text.split(' ')
    word = textList[index]
    return word


def main():
    text = input('Enter text (no full stop): ')
    index = int(input('Enter Index:'))
    try:
        result = readWord(text, index)
        print('Word at position {0} is {1}'.format(index+1, result))
    except IndexError:
        print("Invalid Index Error")


main()
