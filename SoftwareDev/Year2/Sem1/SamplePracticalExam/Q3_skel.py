

from tkinter import *
window = Tk()
window.geometry("300x350")
window.title("Welcome")

class Quad:

    def __init__(self, val1, val2, val3, val4):
        self.__value1 = val1
        self.__value2 = val2
        self.__value3 = val3
        self.__value4 = val4

    def resetAll(self, val):
        self.__value1 = val
        self.__value2 = val
        self.__value3 = val
        self.__value4 = val

    def getValue1(self):
        return self.__value1

    def getValue2(self):
        return self.__value2

    def getValue3(self):
        return self.__value3

    def getValue4(self):
        return self.__value4

    def add(self):
        return self.__value1 + self.__value2 + self.__value3 + self.__value4

    def subFirstLast(self):
        return self.__value1 - self.__value4


#------------end of class definition------------------

def display():
    value1 = c1.getValue1()
    value2 = c1.getValue2()
    value3 = c1.getValue3()
    value4 = c1.getValue4()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry4b.delete(0, END)  # delete old value
    entry4b.insert(END, value4)


def subEvent():
    result= c1.subFirstLast()
    display()
    entry7.delete(0, END)  # delete old value
    entry7.insert(END, result)

def addEvent():
    result = c1.add()
    display()
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, result)


def resetEvent():
    value = int(entry5.get())
    c1.resetAll(value)
    display()


c1 = Quad(7, 5, 4, 2)


label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value1", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=140, y=80)

label3 = Label(window, text="Value2", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=140, y=110)

label4 = Label(window, text="Value3", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=150)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=140, y=150)

label4b = Label(window, text="Value4", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4b.place(x=10, y=190)

entry4b = Entry(window)
entry4b.insert(END, '1')
entry4b.place(x=140, y=190)


button0 = Button(window, text="resetAll", fg="black", font=("arial", 10, ), command=resetEvent)
button0.place(x=10, y=230)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=140, y=230)


button6 = Button(window, text="addAll", fg="black", font=("arial", 10), command=addEvent)
button6.place(x=10, y=270)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=140, y=270)

button7 = Button(window, text="Sub Value1-Value4", fg="black", font=("arial", 10), command=subEvent)
button7.place(x=10, y=310)

entry7 = Entry(window)
entry7.insert(END, '1')
entry7.place(x=140, y=310)
display()

mainloop()
