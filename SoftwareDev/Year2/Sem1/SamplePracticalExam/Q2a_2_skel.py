from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

def add():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    value3 = int(entry5.get())
    result = value1 + value2 + value3
    entry4.delete(0, END)
    entry4.insert(END, result)

def min():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    value3 = int(entry5.get())
    if value2 > value1 < value3:
        entry6.delete(0, END)
        entry6.insert(END, value1)
    elif value1 > value2 < value3:
        entry6.delete(0, END)
        entry6.insert(END, value2)
    elif value1 > value3 < value2:
        entry6.delete(0, END)
        entry6.insert(END, value3)

label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value1 ", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=100, y=80)

label3 = Label(window, text="Value2 ", fg="blue", width=10, font=("arial", 12, "bold"))   #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=100, y=110)

label4 = Label(window, text="Value3 ", fg="blue", width=10, font=("arial", 12, "bold"))   #
label4.place(x=10, y=140)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=100, y=140)


button1 = Button(window, text="add", fg="black", font=("arial", 10, "bold"), command=add)
button1.place(x=40, y=170)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=100, y=170)

button2 = Button(window, text="Min", fg="black", font=("arial", 10, "bold"), command=min)
button2.place(x=40, y=200)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=100, y=200)


mainloop()
