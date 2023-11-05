from random import randint, random


class CannotSetFastestLap(Exception): pass

class NoRacesComplete(Exception): pass


class Driver:
    def __init__(self, name, constructor):
        self.__name = name
        self.__constructor = constructor
        self.__points = 0
        self.__races = 0
        self.__wins = 0
        self.__top10 = 0
        self.__dnf = 0

    def resetAll(self):
        self.__points = 0
        self.__races = 0
        self.__wins = 0
        self.__top10 = 0
        self.__dnf = 0


    def getName(self):
        return self.__name

    def getConstructor(self):
        return self.__constructor
    def getPoints(self):
        return self.__points

    def getNumOfRaces(self):
        return self.__races

    def getNumOfWins(self):
        return self.__wins

    def getNumOfTop10(self):
        return self.__top10

    def getNumOfDNF(self):
        return self.__dnf

    def setPoints(self, position, fastestLapBonus):
        if position > 10 and fastestLapBonus == 1:
            raise CannotSetFastestLap
        else:
            self.__points += fastestLapBonus
            self.__races += 1
            if position == 10:
                self.__points += 1
                self.__top10 += 1
            elif position == 9:
                self.__points += 2
                self.__top10 += 1
            elif position == 8:
                self.__points += 4
                self.__top10 += 1
            elif position == 7:
                self.__points += 6
                self.__top10 += 1
            elif position == 6:
                self.__points += 8
                self.__top10 += 1
            elif position == 5:
                self.__points += 10
                self.__top10 += 1
            elif position == 4:
                self.__points += 12
                self.__top10 += 1
            elif position == 3:
                self.__points += 15
                self.__top10 += 1
            elif position == 2:
                self.__points += 18
                self.__top10 += 1
            elif position == 1:
                self.__points += 25
                self.__top10 += 1
                self.__wins += 1

    def markDNF(self):
        self.__races += 1
        self.__dnf += 1

    def getWinPercentage(self):
        if self.__races == 0:
            raise NoRacesComplete
        else:
            return int(100 * (self.__wins / self.__races))

    def getTop10Percentage(self):
        if self.__races == 0:
            raise NoRacesComplete
        else:
            return int(100 * (self.__top10 / self.__races))

    def getDNFPercentage(self):
        if self.__races == 0:
            raise NoRacesComplete
        else:
            return int(100 * (self.__dnf / self.__races))

    def simSeason(self):
        # self.__points = 0
        # self.__races = 0
        # self.__wins = 0
        # self.__top10 = 0
        # self.__dnf = 0
        # TODO - iterate through 23 races and randomise result
        # TODO - make sure total races is 23
        # TODO - wins are included in the top 10 stat
        # TODO - calculate points based on # races
        # TODO - randomise getting fastest lap

        # TODO - figure out a way to compare race wins across all drivers so duplicates aren't allowed
        # self.__wins = randint(0, 24)
        # self.__top10 = randint(0, 24)
        # self.__dnf = randint(0, 24)

        # POSSIBLE SOLUTION. NOT 100% WORKING
        # num = 0
        # total = 0
        # while num < 23:
        #    if total == 23:
        #        break
        #    randomise = randint(0, 1)
        #    self.__wins += randomise
        #    self.__top10 += randomise
        #    self.__dnf += randomise

        #    total += self.__wins
        #    total += self.__top10
        #    total += self.__dnf

        #    self.__races += 1
        #    num += 1


        # while self.__races < 23:
        #   self.__wins += randint(0, 1)
        #  self.__top10 += randint(0, 1)
        # self.__dnf += randint(0, 1)
            #sum = (self.__wins + self.__top10 + self.__dnf)
        #    # total -= (self.__wins + self.__top10 + self.__dnf)
         #   if (self.__wins + self.__top10 + self.__dnf == 23):
          #      break
           # else:
            #    self.__races += 1
        # print("Loop ended after: " + str(self.__races))
        num = 0
        while num < 23:
            if 0 >= random() < 0.15:
                self.__wins += 1
                self.__top10 += 1
                self.__races += 1
            elif 0.15 >= random() < 0.40:
                self.__top10 += 1
                self.__races += 1
            elif 0.40 >= random() < 0.85:
                self.__races += 1
            elif 0.85 >= random() < 1:
                self.__dnf += 1
                self.__races += 1

            num += 1
            print(num)





