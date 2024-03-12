class MyList:

    def __init__(self,list):
        self._list = list

    def linearSearch(self, target):
        result = False
        for el in self._list:
            if el == target:
                result = True
        return result


    def readList(self):
        list=' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list





