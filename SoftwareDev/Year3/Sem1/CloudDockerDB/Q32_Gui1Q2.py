
#import sqlite3
import pymysql
from tkinter import *


from Q32_Gui2Q2Dialog import *

window = Tk()
window.geometry("300x350")
window.title("Welcome")

#============================================================
# General Methods to Display Data


def setScore_0_Cmd():
    global current
    global product
    cur.execute("select * from testapp.Teams")
    currentTeam = cur.fetchall()[current]
    teamName = currentTeam[0]
    teamScore = currentTeam[1]

    cur.execute("Update testapp.Teams set score=0 where name = \'" + teamName + "\'")

    con.commit()
    display(current)


def highestScoreCmd():
    global current
    global product
    cur.execute("select max(score) from testapp.Teams")
    score = cur.fetchall()[0][0]
    con.commit()
    print("Not here")
    print(score)
    entry2.insert(END, 3)
    display(current)
    entry5b.delete(0, END)
    entry5b.insert(END, score)


def updateScoreCmd():
    global current
    global product
    cur.execute("select * from testapp.Teams")
    currentTeam=cur.fetchall()[current]
    teamName=currentTeam[0]
    teamScore=currentTeam[1]

    newScore = entry5a.get()

    cur.execute("Update testapp.Teams set score=" + newScore + " where name =\'" + teamName + "\'")

    con.commit()
    display(current)


def stepScoreCmd():
    global current
    global product
    cur.execute("select * from testapp.Teams")
    currentTeam=cur.fetchall()[current]
    teamName=currentTeam[0]
    teamScore=currentTeam[1]

    cur.execute("Update testapp.Teams set score=score + 1 where name = \'"+teamName +"\'")

    con.commit()
    display(current)

def displayChange():
    global current
    display(current)

def display(index):
    print('here')
    global current
    global product
    cur.execute("select * from testapp.Teams")
    currentTeam=cur.fetchall()[index]
    #print(currentMovie[0], currentMovie[1])
    current = index
    entry2.delete(0, END)
    entry2.insert(END, currentTeam[0])
    entry3.delete(0, END)
    entry3.insert(END, currentTeam[1])








# End of Method Declarations
#========================================================================
# Database Setup
#con = sqlite3.connect("../../Downloads/tutorial.db")
#cur = con.cursor()

con = pymysql.connect(db='testapp', user='root', passwd='admin', host='localhost',port=3306)
cur = con.cursor()


#========= Definitions ============================




#-------Event Handling Methods ---------------

def teamsDisplay():
    cur.execute("select * from testapp.Teams")
    allTeams = cur.fetchall()
    displayDialog(window, allTeams)


def deleteCurrentCmd():
    try:
        team=entry2.get()
        cur.execute("Delete from testapp.Teams where name = \'" + team + "\'")
        con.commit()
        cur.execute("select * from testapp.Teams")
        allTeams = cur.fetchall()
        display(len(allTeams) - 1)
    except:
        print('Team: ', team, ' does not exist in Database')






def nextCmd():
    global current
    cur.execute("select * from testapp.Teams")
    allTeams=cur.fetchall()
    if (current<(len(allTeams)-1) ):
        current += 1
        display(current)

def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


# ----- Menu Event Handling -----------

def closeCmd():
    exit()



def clearCmd():
    entry2.delete(0, END)
    entry3.delete(0, END)


def insertCmd():
    teamname=entry2.get()
    teamscore=entry3.get()
    cur.execute("INSERT INTO testapp.Teams VALUES(\'" + teamname+ "\' , " + teamscore+")")

    cur.execute("select * from testapp.Teams")
    allTeams=cur.fetchall()
    display(len(allTeams)-1)
    con.commit()

#-----------End of Event Handling


#=======================================================
# Menu to Add New Student
menu1 = Menu(window) #MenuBar
window.config(menu=menu1)
subm1=Menu(menu1)  #Menu
menu1.add_cascade(label="Admin", menu=subm1)
subm1.add_command(label="Delete Team", font=("arial", 11, "bold"), command = deleteCurrentCmd)   # menu item
subm1.add_command(label="Close", font=("arial", 11, "bold"), command = closeCmd)

#======= End of Menu Definition ============================








frame = Frame(window, width=200, height=200)
frame.place(x=10,y=80)

label1 = Label(window, text="Team Application", fg="blue",bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Team", fg="blue",width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Score", fg="blue",width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

button41 = Button(frame, text="StepScore", fg="black", font=("arial", 10, "bold"), command=stepScoreCmd)
button41.grid(row=2, column=0, sticky=W+E)

button42 = Button(frame, text="SetScore 0", fg="black", font=("arial", 10, "bold"), command=setScore_0_Cmd)
button42.grid(row=2, column=1, sticky=W+E)

button5a = Button(frame, text="SetScore to ------->", fg="black", font=("arial", 10, "bold"), command=updateScoreCmd)
button5a.grid(row=3, column=0, sticky=W+E)

entry5a = Entry(frame)
entry5a.insert(END, '0')
entry5a.grid(row=3, column=1, sticky=W+E)


button5b = Button(frame, text="Highest Score ------>", fg="black", font=("arial", 10, "bold"), command=highestScoreCmd)
button5b.grid(row=4, column=0, sticky=W+E)

entry5b = Entry(frame)
entry5b.insert(END, '0')
entry5b.grid(row=4, column=1, sticky=W+E)



labelBlank = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=5, column=0, columnspan=2,sticky=W+E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=6, column=0, sticky=W+E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=6, column=1, sticky=W+E)

button7 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearCmd)
button7.grid(row=7, column=0, sticky=W+E)

button8 = Button(frame, text="InsertItem", fg="black", font=("arial", 10, "bold"), command=insertCmd)
button8.grid(row=7, column=1, sticky=W+E)


labelBlank2 = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank2.grid(row=9, column=0, columnspan=2,sticky=W+E)


cur.execute("select * from testapp.Teams")
allTeams = cur.fetchall()
button12 = Button(frame, text="Display allTeams", fg="black", font=("arial", 10, "bold"), command=teamsDisplay)
button12.grid(row=10, column=0, columnspan=2, sticky=W+E)

display(0)


mainloop()




