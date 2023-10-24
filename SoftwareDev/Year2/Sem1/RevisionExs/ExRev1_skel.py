

def main():
    count = 0
    result = 0

    while count < 8:
        val = int(input("Enter Value {0}:".format(count + 1)))
        if val >= 10 and val <= 99:
            result += 1
        count += 1
 
    print('Number of Double Digit Numbers = {0}'.format(result))


main()
