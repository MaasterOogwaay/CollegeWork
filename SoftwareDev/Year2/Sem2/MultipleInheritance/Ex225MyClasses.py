#---------------------------------------------

class Coach:

        def __init__(self, title, licence):
            self._title = title
            self._licence = licence

        def getTitle(self):
            return self._title

        def getLicence(self):
            return self._licence

        def setLicence(self, licence):
            self._licence = licence

class Player:

    def __init__(self, position, gamesPlayed):
        self._position = position
        self.__gamesPlayed = gamesPlayed


    def getPosition(self):
        return self._position

    def getGamesPlayed(self):
        return self.__gamesPlayed

    def setGamesPlayed(self, gamesPlayed):
        self.__gamesPlayed = gamesPlayed


# Extended Class
class PlayerCoach(Coach, Player):
    def __init__(self, name, title, license, position, played):
        Coach.__init__(self, title, license)
        Player.__init__(self, position, played)
        self.__name = name

    def incrementGamesPlayed(self):
        played = Player.getGamesPlayed(self)
        incremented = played + 1
        Player.setGamesPlayed(self, incremented)


    def getName(self):
        return self.__name

    def setTitle(self, title):
        self._title = title
