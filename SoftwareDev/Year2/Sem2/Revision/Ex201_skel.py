

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

class Counter:

    def __init__(self, val, amt):   #***
        self.__value = val
        self.__amount = amt

    def setValue(self,val):
        self.__value=val

    def getValue(self):
        return self.__value

    def getAmount(self):
        return self.__amount

    def resetAmount(self, amt):
        self.__amount = amt

    def subtractAmount(self):
        if (self.__amount <= self.__value):
            self.__value -= self.__amount
            return True
        else:
            return False

    def addAmount(self):
        self.__value += self.__amount


#------------end of class definition------------------

def display():
    value = c1.getValue()
    amount = c1.getAmount()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, amount)
    entry5.delete(0, END)  # delete old value



def addEvent():
    c1.addAmount()
    display()
    entry4.delete(0, END)  # delete old value

def subEvent():
    result= c1.subtractAmount()
    display()
    entry4.delete(0, END)  # delete old value

    if (result==False):
        entry4.insert(END, 'Too Low')
    else:
        entry4.insert(END, 'Success')


def resetEvent():
    newAmount = int(entry5.get())
    c1.resetAmount(newAmount)
    display()
    entry4.delete(0, END)  # delete old value

c1=Counter(8,2)


label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text=" Amount", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)


button1 = Button(window, text="Add Amount", fg="black", font=("arial", 9, "bold"), command=addEvent)
button1.place(x=40, y=140)

button2 = Button(window, text="Sub Amount", fg="black", font=("arial", 9, "bold"), command=subEvent)
button2.place(x=140, y=140)

label4 = Label(window, text="Message", fg="blue", width=8, font=("arial", 10, "bold"))   #
label4.place(x=10, y=180)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=180)

button3 = Button(window, text="Reset Amount", fg="black", font=("arial", 9, "bold"), command=resetEvent)
button3.place(x=10, y=220)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=220)

display()

mainloop()
