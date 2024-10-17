def main():
    val1 = int(input('Enter Value1: '))
    val2 = int(input('Enter Value2: '))
    val3 = int(input('Enter Value3: '))
    result1 = hCount( pIsEven ,val1, val2,val3)
    print('Number  of Even Items=', result1)
    result2 = hCount( pSingleDigit ,val1, val2,val3)
    print('Number of Single Digits=', result2)

pIsEven = lambda x: (x%2 == 0)

pSingleDigit = lambda y: y < 10

def hCount(f,a,b, c):
    result = 0
    if (f(a)):
        result += 1
    if (f(b)):
        result += 1
    if (f(c)):
        result += 1
    return result


main()
