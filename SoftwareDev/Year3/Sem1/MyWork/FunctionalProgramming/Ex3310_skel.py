def main():
    studentJohn = my_print('John')
    studentMary = my_print('Mary')
    studentPeter= my_print('Tony')

    studentJohn('Shine')
    studentMary('Dunning')
    studentPeter('Jones')
    studentPeter('Smith')


def my_print(first):
    def print_last(last):
        return print("Full Name:= " + first + " " + last)
    return print_last


main()
