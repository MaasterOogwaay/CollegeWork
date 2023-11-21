def main():
    list1= [-2, -5, -2, -8, -7]
    next1=int(input('Enter next Item: '))
    list1.append(next1)
    next2=int(input('Enter next Item: '))
    list1.append(next2)

    result = allNegative(list1)
    print('All Item in list are negative = {0}'.format(result))

def allNegative(listp):
    result = True
    for i in listp:
        if i >= 0:
            result = False
    return result

main()
