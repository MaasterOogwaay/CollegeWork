from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

def add():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    result = value1 + value2
    entry4.delete(0, END)
    entry4.insert(END, result)

def isEqual():
    result = "False"
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    if value1 == value2:
        result = "True"
    entry5.delete(0, END)
    entry5.insert(END, result)

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


button1 = Button(window, text="add", fg="black", font=("arial", 10, "bold"), command=add)
button1.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=100, y=140)


button2 = Button(window, text="Equal", fg="black", font=("arial", 10, "bold"), command=isEqual)
button2.place(x=40, y=170)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=100, y=170)


mainloop()
