def main():
    height = int(input('Enter Height: '))
    display(height)


def display(h):
    for values in range(1, h + 1):
        print("*")


main()
