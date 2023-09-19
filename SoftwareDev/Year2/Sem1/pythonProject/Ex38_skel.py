def main():
    width = int(input('Enter Width: '))
    display(width)


def display(w):
    for values in range(1, w + 1):
        print("* ", end="")


main()
