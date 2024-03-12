class MyList:

    def __init__(self, list):
        self._list = list

    def binarySearch(self, target):
        LI = 0
        UI = len(self._list)-1
        mid = int((LI+UI)/2)
        found = False
        while LI < UI and found == False:

            print("LI = " + str(LI))
            print("MID = " + str(mid))
            print("UI = " + str(UI))

            if target == self._list[mid]:
                found = True
            elif target < self._list[mid]:
                UI = mid - 1
            elif target > self._list[mid]:
                LI = mid + 1
            mid = int((LI + UI) / 2)

        return found

    def readList(self):
        self._list = sorted(self._list)
        list = ' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list
