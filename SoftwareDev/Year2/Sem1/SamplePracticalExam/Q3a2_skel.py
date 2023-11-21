

from tkinter import *
window = Tk()
window.geometry("300x350")
window.title("Welcome")

class Hotel:

    def __init__(self, hotelName, city, maxGuests):
        self.__hotel = hotelName
        self.__city = city
        self.__maxGuests = maxGuests
        self.__numOfGuests = 0

    def getName(self):
        return self.__hotel

    def getCity(self):
        return self.__city

    def getMaxGuests(self):
        return self.__maxGuests

    def getNumberGuests(self):
        return self.__numOfGuests

    def addGuests(self, amount):
        if (self.__numOfGuests + amount) > self.__maxGuests:
            return False
        else:
            self.__numOfGuests += amount
            return True

    def resetName(self, name):
        self.__hotel = name


# ------------end of class definition------------------

def display():
    value1 = c1.getName()
    value2 = c1.getCity()
    value3 = c1.getMaxGuests()
    value4 = c1.getNumberGuests()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, str(value3))
    entry4b.delete(0, END)  # delete old value
    entry4b.insert(END, str(value4))
    entry5b.delete(0, END)  # delete old value
    entry5b.insert(END, '')


def addEvent():
    amt = int(entry6.get())
    result = c1.addGuests(amt)
    display()
    if result == False:
        entry5b.insert(END, 'Insuff Space')


def resetEvent():
    newName = entry5.get()
    c1.resetName(newName)
    display()


c1 = Hotel("Gresham", "Dublin", 300)


label1 = Label(window, text="Hotel Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="City", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="MaxGuests", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=150)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=150)

label4b = Label(window, text="CurrentNo", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4b.place(x=10, y=190)

entry4b = Entry(window)
entry4b.insert(END, '1')
entry4b.place(x=120, y=190)

button0 = Button(window, text="resetName", fg="black", font=("arial", 10, ), command=resetEvent)
button0.place(x=10, y=230)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=230)


button6 = Button(window, text="addGuests", fg="black", font=("arial", 10), command=addEvent)
button6.place(x=10, y=270)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=270)

label5b = Label(window, text="Error", fg="blue", width=8, font=("arial", 10, "bold"))   #
label5b.place(x=10, y=310)

entry5b = Entry(window)
entry5b.insert(END, '1')
entry5b.place(x=120, y=310)

display()

mainloop()
