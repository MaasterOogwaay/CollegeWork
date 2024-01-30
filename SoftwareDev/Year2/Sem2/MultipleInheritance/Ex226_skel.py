

from tkinter import *
window = Tk()
window.geometry("300x360")
window.title("Welcome")

from Ex226MyClasses import *


#------------end of class definition------------------

def display():
    value1 = t1.getMake()
    value2 = t1.getModel()
    value3 = t1.getEngine()
    value4 = t1.getBeds()
    value5 = t1.getAirCond()
    value6 = t1.getSeats()
  ##  t1.
    # make, model, engine, beds, airCond, seats
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)
    entry6.delete(0, END)  # delete old value
    if (value5==1):
        entry6.insert(END, 'True')
    else:
        entry6.insert(END, 'False')
    entry6b.delete(0, END)  # delete old value
    entry6b.insert(END, value6)



def addBedsEvent():
    newBeds = int(entry3a.get())
    t1.addBeds(newBeds)
    display()


def updateSeatsEvent():
    newSeats = entry3b.get()
    t1.setSeats(newSeats)
    display()

def airCondEvent():
    t1.setAirCond(True)
    display()

def noAirCondEvent():
    t1.setAirCond(False)
    display()

t1=CamperVan("VW","California",2100, 3,True, 5)


label1 = Label(window, text="CamperVan Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=40, y=30)                            # place on screen

label2 = Label(window, text="Make", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=130, y=80)

label3 = Label(window, text="Model", fg="blue", width=12, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=130, y=110)

label4 = Label(window, text="Engine", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=130, y=140)

label5 = Label(window, text="Beds", fg="blue", width=12, font=("arial", 10, "bold"))   #
label5.place(x=10, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=130, y=170)

label6 = Label(window, text="Air Condition", fg="blue", width=11, font=("arial", 10, "bold"))   #
label6.place(x=10, y=200)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=130, y=200)

label6b = Label(window, text="Seats", fg="blue", width=11, font=("arial", 10, "bold"))   #
label6b.place(x=10, y=230)

entry6b = Entry(window)
entry6b.insert(END, '')
entry6b.place(x=130, y=230)


#-------------------------------
button1= Button(window, text="addBeds", fg="black", font=("arial", 10, "bold"), command=addBedsEvent)
button1.place(x=2, y=260)

entry3a = Entry(window)
entry3a.insert(END, '2')
entry3a.place(x=130, y=260)

#button2= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
#button2.place(x=120, y=230)

button3= Button(window, text="updateSeats", fg="black", font=("arial", 10, "bold"), command=updateSeatsEvent)
button3.place(x=2, y=290)

entry3b = Entry(window)
entry3b.insert(END, '6')
entry3b.place(x=130, y=290)

button4= Button(window, text="mark AirCond", fg="black", font=("arial", 10, "bold"), command=airCondEvent)
button4.place(x=2, y=320)

button5= Button(window, text="mark NoAirCond", fg="black", font=("arial", 10, "bold"), command=noAirCondEvent)
button5.place(x=130, y=320)



display()

mainloop()
