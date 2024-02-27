def main():
    # studentList= {'Smith':58, 'Jones':36, 'peters':78, 'Adams':44}
    studentList = {1234: 'Smith', 23123: 'Jones', 8834: 'Peters', 1212: 'Smith'}
    studentList.update({8292: 'Smith'})
    studentList.update({4321: 'Jones'})
    name = input('Enter Name to Search for: ')
    result = countOccurs(studentList, name)
    print('Student {0} occurs {1} times'.format(name, result))


def countOccurs(studentL, name):
    result = 0
    for key, value in studentL.items():
        if value == name:
            result += 1

    return result


main()
