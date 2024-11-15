from tkinter import *
from drivers import (Driver, CannotSetFastestLap, NoRacesComplete, MaxRaceLimitReached, SimSeasonFailed, LeaderboardDataErr)

window = Tk()
window.geometry("380x580")
window.title("Welcome")

# =====| Event Handlers |=====


def display(index):
    global current
    global driver
    driver = driverList[index]
    current = index

    driverNameEntry.delete(0, END)
    driverNameEntry.insert(END, driver.getName())
    constructorNameEntry.delete(0, END)
    constructorNameEntry.insert(END, driver.getConstructor())
    numOfPointsEntry.delete(0, END)
    numOfPointsEntry.insert(END, driver.getPoints())
    numOfRacesEntry.delete(0, END)
    numOfRacesEntry.insert(END, driver.getNumOfRaces())
    numOfWinsEntry.delete(0, END)
    numOfWinsEntry.insert(END, driver.getNumOfWins())
    numOfTop10Entry.delete(0, END)
    numOfTop10Entry.insert(END, driver.getNumOfTop10())
    numOfDNFEntry.delete(0, END)
    numOfDNFEntry.insert(END, driver.getNumOfDNF())


def setPoints():
    try:
        fastestLapBonus = 0
        if var_fastestLapCheckbox.get() == 1:
            fastestLapBonus = 1
        position = int(positionVar.get())
        driver.setPoints(position, fastestLapBonus)
        display(current)
    except CannotSetFastestLap:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "Cannot set fastest lap when position > 10")
    except MaxRaceLimitReached:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "Max number of races reached")


def markDNF():
    try:
        driver.markDNF()
        display(current)
    except MaxRaceLimitReached:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "Max number of races reached")


def resetData():
    global current
    for el in driverList:
        el.resetAll()
    winPercentageEntry.delete(0, END)
    top10PercentageEntry.delete(0, END)
    dnfPercentageEntry.delete(0, END)
    bestDriverEntry.delete(0, END)
    errorMessageEntry.delete(0, END)
    display(current)


def getWinPercentage():
    try:
        result = driver.getWinPercentage()
        winPercentageEntry.delete(0, END)
        winPercentageEntry.insert(END, (str(result) + " %"))
    except NoRacesComplete:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "No races complete")


def getTop10Percentage():
    try:
        result = driver.getTop10Percentage()
        top10PercentageEntry.delete(0, END)
        top10PercentageEntry.insert(END, (str(result) + " %"))
    except NoRacesComplete:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "No races complete")


def getDNFPercentage():
    try:
        result = driver.getDNFPercentage()
        dnfPercentageEntry.delete(0, END)
        dnfPercentageEntry.insert(END, (str(result) + " %"))
    except NoRacesComplete:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "No races complete")


def simulateSeason():
    global driver
    global current
    try:
        for el in driverList:
            el.simSeason()
        errorMessageEntry.insert(END, "Sim season complete")
        display(current)

    except SimSeasonFailed:
        errorMessageEntry.insert(END, "Sim season failed")


def getLeaderboardData():
    global driver
    try:
        rowX = 1
        x = []
        for el in driverList:
            testing = el.getLeaderboardData()
            x.append(testing)

        x.sort(key=lambda y: y[1], reverse=True)

        for content in x:
            rowX += 1
            print(content[0])
            posBox = Entry(frame2)
            posBox.grid(column=0, row=rowX)
            posBox.delete(0, END)
            posBox.insert(END, str(rowX - 1))

            nameBox = Entry(frame2)
            nameBox.grid(column=1, row=rowX)
            nameBox.delete(0, END)
            nameBox.insert(END, content[0])

            pointsBox = Entry(frame2)
            pointsBox.grid(column=2, row=rowX)
            pointsBox.delete(0, END)
            pointsBox.insert(END, content[1])

    except LeaderboardDataErr:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "Leaderboard data err")


def getBestDriver():
    global driver
    try:
        largest = 0
        name = ""
        for el in driverList:
            if el.getPoints() > largest:
                largest = el.getPoints()
                name = el.getName()

        bestDriverEntry.delete(0, END)
        bestDriverEntry.insert(END, name)
        errorMessageEntry.insert(END, "Leader data collected")
    except LeaderboardDataErr:
        errorMessageEntry.delete(0, END)
        errorMessageEntry.insert(END, "Leaderboard data err")


def prevCmd():
    global current
    if current > 0:
        current -= 1
        display(current)


def nextCmd():
    global current
    if current < (len(driverList) - 1):
        current += 1
        display(current)


def firstCmd():
    display(0)


def lastCmd():
    display(len(driverList) - 1)

# =====| SWAP PAGES |=====


def changeToDriver():
    frame.pack(fill='both', expand=1)
    frame2.pack_forget()


def changeToLeaderboard():
    frame2.pack(fill='both', expand=1)
    frame.pack_forget()
    getLeaderboardData()
# =====| END OF SWAP PAGES |=====

# =====| End of Event Handlers |=====


# =====| Definitions |=====
driver1 = Driver("Max Verstappen", "Red Bull Racing")
driver2 = Driver("Sergio Perez", "Red Bull Racing")
driver3 = Driver("Lewis Hamilton", "Mercedes")
driver4 = Driver("Carlos Sainz", "Ferrari")
driver5 = Driver("Fernando Alonso", "Aston Martin")
driver6 = Driver("Lando Norris", "McLaren")
driver7 = Driver("Charles Leclerc", "Ferrari")
driver8 = Driver("Oscar Piastri", "McLaren")
driver9 = Driver("Pierre Gasly", "Alpine")
driver10 = Driver("Lance Stroll", "Aston Martin")
driver11 = Driver("Esteban Ocon", "Alpine")
driver12 = Driver("Alexander Albon", "Williams")
driver13 = Driver("Valtteri Bottas", "Alfa Romeo")
driver14 = Driver("Nico Hulkenberg", "Haas F1 Team")
driver15 = Driver("Yuki Tsunoda", "AlphaTauri")
driver16 = Driver("Daniel Ricciardo", "AlphaTauri")
driver17 = Driver("Zhou Guanyu", "Alfa Romeo")
driver18 = Driver("Kevin Magnussen", "Haas F1 Team")
driver19 = Driver("George Russell", "Mercedes")
driver20 = Driver("Logan Sargeant", "Williams")

driverList = [driver1, driver2, driver3, driver4, driver5, driver6, driver7, driver8, driver9, driver10, driver11,
              driver12, driver13, driver14, driver15, driver16, driver17, driver18, driver19, driver20]
global current
global driver
driver = driverList[0]
# =====| End of Definitions |=====

# =====| Menus |=====
menu1 = Menu(window)
window.config(menu=menu1)
menu1.add_command(label="Driver Standings",  font=("arial", 12, "bold"), command=changeToDriver)   # menu item
menu1.add_command(label="Leaderboard", font=("arial", 12, "bold"), command=changeToLeaderboard)
# =====| End of Menus |=====

frame = Frame(window)

# =====| TESTING |=====
frame2 = Frame(window)
# =====| END |=====

# =====| Driver Standings Page |=====
titleLabel = Label(frame, text="F1 Standings", fg="blue", bg="yellow", font=("arial", 16, "bold"))
titleLabel.grid(row=0, column=0, columnspan=2, sticky=W+E)

driverNameLabel = Label(frame, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
driverNameLabel.grid(row=1, column=0, sticky=W+E)
driverNameEntry = Entry(frame)
driverNameEntry.insert(END, ' ')
driverNameEntry.grid(row=1, column=1, sticky=W+E)

constructorNameLabel = Label(frame, text="Constructor", fg="blue", width=15, font=("arial", 10, "bold"))
constructorNameLabel.grid(row=2, column=0, sticky=W+E)
constructorNameEntry = Entry(frame)
constructorNameEntry.insert(END, ' ')
constructorNameEntry.grid(row=2, column=1, sticky=W+E)

numOfPointsLabel = Label(frame, text="# of Points", fg="blue", width=15, font=("arial", 10, "bold"))
numOfPointsLabel.grid(row=3, column=0, sticky=W+E)
numOfPointsEntry = Entry(frame)
numOfPointsEntry.insert(END, '0')
numOfPointsEntry.grid(row=3, column=1, sticky=W+E)

numOfRacesLabel = Label(frame, text="# of Races", fg="blue", width=15, font=("arial", 10, "bold"))
numOfRacesLabel.grid(row=4, column=0, sticky=W+E)
numOfRacesEntry = Entry(frame)
numOfRacesEntry.insert(END, '0')
numOfRacesEntry.grid(row=4, column=1, sticky=W+E)

numOfWinsLabel = Label(frame, text="# of Wins", fg="blue", width=15, font=("arial", 10, "bold"))
numOfWinsLabel.grid(row=5, column=0, sticky=W+E)
numOfWinsEntry = Entry(frame)
numOfWinsEntry.insert(END, '0')
numOfWinsEntry.grid(row=5, column=1, sticky=W+E)

numOfTop10Label = Label(frame, text="# of Top 10", fg="blue", width=15, font=("arial", 10, "bold"))
numOfTop10Label.grid(row=6, column=0, sticky=W+E)
numOfTop10Entry = Entry(frame)
numOfTop10Entry.insert(END, '0')
numOfTop10Entry.grid(row=6, column=1, sticky=W+E)

numOfDNFLabel = Label(frame, text="# of DNF's", fg="blue", width=15, font=("arial", 10, "bold"))
numOfDNFLabel.grid(row=7, column=0, sticky=W+E)
numOfDNFEntry = Entry(frame)
numOfDNFEntry.insert(END, '0')
numOfDNFEntry.grid(row=7, column=1, sticky=W+E)


labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=8, column=0, columnspan=2, sticky=W+E)


var_fastestLapCheckbox = IntVar()  # 0 unchecked, 1 checked
fastestLapCheckbox = Checkbutton(frame, text="Fastest Lap", variable=var_fastestLapCheckbox)
fastestLapCheckbox.grid(row=9, column=0, columnspan=2)

recordPositionButton = Button(frame, text="Record Position", fg="black", font=("arial", 10, "bold"), command=setPoints)
recordPositionButton.grid(row=10, column=0, sticky=W+E)
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
positionVar = StringVar()
combo1 = OptionMenu(frame, positionVar, *list1)
positionVar.set("1")
combo1.grid(row=10, column=1, sticky=W+E)

recordDNFButton = Button(frame, text="Record DNF", fg="black", font=("arial", 10, "bold"), command=markDNF)
recordDNFButton.grid(row=11, column=0, sticky=W+E)

resetDataButton = Button(frame, text="Reset Data", fg="black", font=("arial", 10, "bold"), command=resetData)
resetDataButton.grid(row=11, column=1, sticky=W+E)


labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=12, column=0, columnspan=2, sticky=W+E)


winPercentageButton = Button(frame, text="Calculate Win %", fg="black", font=("arial", 10, "bold"), command=getWinPercentage)
winPercentageButton.grid(row=13, column=0, sticky=W+E)
winPercentageEntry = Entry(frame)
winPercentageEntry.insert(END, '0')
winPercentageEntry.grid(row=13, column=1, sticky=W+E)

top10PercentageButton = Button(frame, text="Calculate Top 10 %", fg="black", font=("arial", 10, "bold"), command=getTop10Percentage)
top10PercentageButton.grid(row=14, column=0, sticky=W+E)
top10PercentageEntry = Entry(frame)
top10PercentageEntry.insert(END, '0')
top10PercentageEntry.grid(row=14, column=1, sticky=W+E)

dnfPercentageButton = Button(frame, text="Calculate DNF %", fg="black", font=("arial", 10, "bold"), command=getDNFPercentage)
dnfPercentageButton.grid(row=15, column=0, sticky=W+E)
dnfPercentageEntry = Entry(frame)
dnfPercentageEntry.insert(END, '0')
dnfPercentageEntry.grid(row=15, column=1, sticky=W+E)

bestDriverButton = Button(frame, text="Best Driver", fg="black", font=("arial", 10, "bold"), command=getBestDriver)
bestDriverButton.grid(row=16, column=0, sticky=W+E)
bestDriverEntry = Entry(frame)
bestDriverEntry.insert(END, ' ')
bestDriverEntry.grid(row=16, column=1, sticky=W+E)

simSeasonButton = Button(frame, text="Simulate Season", fg="black", font=("arial", 10, "bold"), command=simulateSeason)
simSeasonButton.grid(row=17, column=0, columnspan=2, sticky=W+E)


labelBlank = Label(frame, text=" ", fg="blue", width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=18, column=0, columnspan=2, sticky=W+E)


prevButton = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
prevButton.grid(row=19, column=0, sticky=W+E)

nextButton = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
nextButton.grid(row=19, column=1, sticky=W+E)

firstButton = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
firstButton.grid(row=20, column=0, sticky=W+E)

lastButton = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
lastButton.grid(row=20, column=1, sticky=W+E)

errorMessageLabel = Label(frame, text="Error Message", fg="red", width=15, font=("arial", 10, "bold"))
errorMessageLabel.grid(row=21, column=0, sticky=W+E)
errorMessageEntry = Entry(frame)
errorMessageEntry.insert(END, ' ')
errorMessageEntry.grid(row=21, column=1, sticky=W+E)

# =====| End of Driver Standings Page |=====

# =====| Start of Leaderboard Page |=====
titleLabel = Label(frame2, text="Leaderboard", fg="blue", bg="yellow", font=("arial", 16, "bold"))
titleLabel.grid(row=0, column=0, columnspan=3, sticky=W+E)

positionLabel = Label(frame2, text="Position", fg="blue", width=15, font=("arial", 10, "bold"))
positionLabel.grid(row=1, column=0, sticky=W+E)
driverNameLabel = Label(frame2, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
driverNameLabel.grid(row=1, column=1, sticky=W+E)
driverPointsLabel = Label(frame2, text="Points", fg="blue", width=15, font=("arial", 10, "bold"))
driverPointsLabel.grid(row=1, column=2, sticky=W+E)

# =====| End of Leaderboard Page |=====

display(0)
changeToDriver()
mainloop()
