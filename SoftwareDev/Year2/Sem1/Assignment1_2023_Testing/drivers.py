from random import random, choice
#import random

class CannotSetFastestLap(Exception): pass

class NoRacesComplete(Exception): pass

class MaxRaceLimitReached(Exception): pass


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
        if self.__races == 23:
            raise MaxRaceLimitReached
        elif position > 10 and fastestLapBonus == 1:
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

        # TODO - wins are included in the top 10 stat
        # TODO - calculate points based on # races
        # TODO - randomise getting fastest lap

        # TODO - figure out a way to compare race wins across all drivers so duplicates aren't allowed
        points_list = [18, 15, 12, 10, 8, 6, 4, 2, 1]
        numRaces = 0
        if self.__races > 0:
            numRaces = self.__races
        for i in range(23-numRaces):
            self.__races += 1
            if 0 >= random() < 0.30:
                self.__wins += 1
                self.__top10 += 1
                self.__points += 25
            elif 0.30 >= random() < 0.70:
                self.__top10 += 1
                self.__points += choice(points_list)
            elif 0.70 >= random() < 0.95:
                print("Placed 10-20")
            elif 0.95 >= random() < 1:
                self.__dnf += 1


    def getLeaderboardData(self):
        name = self.__name
        points = self.__points

        print("Name: {0} | Points: {1}".format(name, points))
        return name, points





