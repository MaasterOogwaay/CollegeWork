from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def incr():
    value = int(entry2.get())
    value = value + 1
    entry2.delete(0, END)
    entry2.insert(END, value)


def decr():
    value = int(entry2.get())
    value = value - 1
    entry2.delete(0, END)
    entry2.insert(END, value)


def reset():
    value = int(entry3.get())
    entry2.delete(0, END)
    entry2.insert(END, value)


def add():
    value = int(entry2.get())
    add_value = int(entry4.get())
    value = value + add_value
    entry2.delete(0, END)
    entry2.insert(END, value)

label1 = Label(window, text="Welcome", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=100, y=80)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=110, y=150)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=110, y=190)

button1 = Button(window, text="Increment", fg="black", font=("arial", 12, "bold"), command=incr)
button1.place(x=40, y=110)

button2 = Button(window, text="Decrement", fg="black", font=("arial", 12, "bold"), command=decr)
button2.place(x=150, y=110)

button3 = Button(window, text="Reset", fg="black", font=("arial", 12, "bold"), command=reset)
button3.place(x=40, y=150)

button4 = Button(window, text="Add", fg="black", font=("arial", 12, "bold"), command=add)
button4.place(x=40, y=190)


mainloop()
