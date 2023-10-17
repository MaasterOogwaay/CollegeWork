def main():
   list1 = [2, 5, 2, 8, 7, 3, 2, 5]
   target = int(input('Enter Target: '))
   result = addGreaterTarget(list1, target)
   print('Sum of Items Greater than Target={0}, sum= {1}'.format(target, result))


def addGreaterTarget(listp, tar):
   if len(listp) == 0:
      return 0
   else:
      first = listp.pop(0)
      if first > tar:
         return first + addGreaterTarget(listp, tar)
      else:
         return 0 + addGreaterTarget(listp, tar)


main()
