def main():
    value = 65
    print("  Ascii Table")
    print("---------------")
    print("Letter    Ascii")
    for value in range(65, 100):
        letter = chr(value)
        print("   {0}        {1}".format(letter, value))
        value += 1
        if value == 73:
            break


main()
