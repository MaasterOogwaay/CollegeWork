

from tkinter import *
window = Tk()
window.geometry("300x350")
window.title("Welcome")


def main():
    text = 'the small sized and the medium sized towns'
    target1 = input('Enter First Target word: ')
    target2 = input('Enter Second Target word: ')
    result = countWordsOccurance(text, target1, target2)
    print('{0}, {1}: Occur in text: \"{2}\" {3} times'.format(target1, target2, text, result))


def countWordsOccurance(text, target1, target2):
    result = 0
    # listOfWords = text.split(" ")

    # for word in listOfWords:
    #    if word == target1:
    #        result += 1
    #    elif word == target2:
    #        result += 1

    # numTar1 = listOfWords.count(target1)
    # numTar2 = listOfWords.count(target2)
    # result += numTar1
    # result += numTar2

    countTarget1 = text.count(target1)
    countTarget2 = text.count(target2)
    total = countTarget1 + countTarget2
    result += total

    return result


main()


