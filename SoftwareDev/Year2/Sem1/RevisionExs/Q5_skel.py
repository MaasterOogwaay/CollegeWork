

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

class Calculator:

    def __init__(self, val1, val2):
        self.__value1 = val1
        self.__value2 = val2

    def resetV1(self, val):
        self.__value1 = val

    def resetV2(self, val):
        self.__value2 = val

    def getValue1(self):
        return self.__value1

    def getValue2(self):
        return self.__value2

    def add(self):
        return self.__value1 + self.__value2

    def mult(self):
        return self.__value1 * self.__value2


#------------end of class definition------------------

def display():
    value1 = c1.getValue1()
    value2 = c1.getValue2()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)

def addEvent():
    result= c1.add()
    display()
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, result)



def multEvent():
    result= c1.mult()
    display()
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, result)

def resetEvent1():
    value = int(entry5.get())
    c1.resetV1(value)
    display()

def resetEvent2():
    value = int(entry6.get())
    c1.resetV2(value)
    display()


c1=Calculator(3,4)


label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value1", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value2", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)


button1 = Button(window, text="Add", fg="black", font=("arial", 12, "bold"), command=addEvent)
button1.place(x=40, y=140)

button2 = Button(window, text="Mult", fg="black", font=("arial", 12, "bold"), command=multEvent)
button2.place(x=140, y=140)

label4 = Label(window, text="Result", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=180)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=180)

button5 = Button(window, text="Reset v1", fg="black", font=("arial", 10), command=resetEvent1)
button5.place(x=10, y=230)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=230)

button6 = Button(window, text="Reset v2", fg="black", font=("arial", 10), command=resetEvent2)
button6.place(x=10, y=270)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=270)
display()

mainloop()
