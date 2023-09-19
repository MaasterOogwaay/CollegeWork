def main():
    width = int(input('Enter Width: '))
    display(width)


def display(w):
    for val1 in range(1, w + 1):
        for val2 in range(1, w + 1):
            print("* ", end="")
        print()



main()
