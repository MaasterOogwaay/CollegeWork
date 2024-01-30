#---------------------------------------------

class Caravan:

        def __init__(self, beds, airCond):
            self._beds = beds
            self._airCond = airCond

        def getBeds(self):
            return self._beds

        def getAirCond(self):
            return self._airCond

        def setAirCond(self, airCond):
            self._airCond = airCond

class Car:

    def __init__(self, make, engine):
        self._make = make
        self._engine = engine

    def getMake(self):
        return self._make

    def getEngine(self):
        return self._engine
    # Extended Class


class CamperVan(Caravan, Car):
    def __init__(self, make, model, engine, beds, airCond, seats):
        Caravan.__init__(self, beds, airCond)
        Car.__init__(self, make, engine)
        self.__model = model
        self.__seats = seats

    def getSeats(self):
        return self.__seats

    def getModel(self):
        return self.__model

    def setSeats(self, amt):
        self.__seats = amt

    def addBeds(self, amt):
        self._beds += amt

