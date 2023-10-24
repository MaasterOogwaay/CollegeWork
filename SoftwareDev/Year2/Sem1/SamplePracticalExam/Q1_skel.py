

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def resetV1():

    value2 = int(resetVar1.get())
    entry2.delete(0, END)
    entry2.insert(END, value2)


def resetV2():

    value3 = int(resetVar2.get())
    entry3.delete(0, END)
    entry3.insert(END, value3)


def add():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    sum = value1 + value2
    entry4.delete(0, END)
    entry4.insert(END, sum)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Value1", fg="blue", width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Value2", fg="blue", width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '1')
entry3.grid(row=1, column=1, sticky=W+E)

button1 = Button(frame, text="Reset V1", fg="black", font=("arial", 10, "bold"), command=resetV1)
button1.grid(row=2, column=0, sticky=W+E)

list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
resetVar1 = StringVar()
combo1 = OptionMenu(frame,resetVar1, *list1)
resetVar1.set("1")
combo1.grid(row=2,column=1, sticky=W+E)


button2 = Button(frame, text="Reset V2", fg="black", font=("arial", 10, "bold"), command=resetV2)
button2.grid(row=3, column=0, sticky=W+E)

list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
resetVar2 = StringVar()
combo2 = OptionMenu(frame,resetVar2, *list2)
resetVar2.set("1")
combo2.grid(row=3, column=1, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '1')
entry4.grid(row=4, column=1, sticky=W+E)

button3 = Button(frame, text="Add", fg="black", font=("arial", 10, "bold"), command=add)
button3.grid(row=4, column=0, sticky=W+E)

mainloop()
