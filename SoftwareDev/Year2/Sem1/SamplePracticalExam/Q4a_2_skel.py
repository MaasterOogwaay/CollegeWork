def calculate(value1, value2):
    if value1.isnumeric() and value2.isnumeric():
        result = int(value1) + int(value2)
        return result
    else:
        raise Exception
def main():
    val1 = input("Enter First:")
    val2 = input("Enter Second:")
    try:
        result = calculate(val1, val2)
        print('{0} + {1} = {2}'.format(val1,val2,result))
    except:
        print("Values must be integers")

main()


