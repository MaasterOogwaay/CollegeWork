
class MyList:

    def __init__(self, list):
        self._list = list

    def selectionSort(self):
        for i in range(0, len(self._list)):
            min = i

            for j in range(min + 1, len(self._list)):
                if self._list[j] < self._list[min]:
                    min = j
            (self._list[i], self._list[min]) = (self._list[min], self._list[i])

    def readList(self):
        list = ' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list





