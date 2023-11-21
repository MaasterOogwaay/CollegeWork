def main():
    count=0
    result=0
    while count<10:
        value = int(input("Enter Value {0}:".format(count + 1)))
        if value == 0:
            result += 1
        count += 1
    print("0 occurs in list {0} times".format(result))
main()
