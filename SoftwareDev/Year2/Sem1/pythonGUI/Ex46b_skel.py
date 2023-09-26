from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("300x300")
window.title("Welcome")


def get_price():

    nights = int(entry2.get())
    guests = int(guestVar.get())
    cots = int(cotsVar.get())
    global price
    price = 50*nights
    if cots > 0:
        price = price + (cots*nights*10)
        entry3.delete(0, END)
        entry3.insert(END, price)
    if var_cb1.get() > 0:
        price = price + (guests*10*nights)
        entry3.delete(0, END)
        entry3.insert(END, price)
    if var_cb2.get() > 0:
        price = price + (guests*30*nights)
        entry3.delete(0, END)
        entry3.insert(END, price)
    entry3.delete(0, END)
    entry3.insert(END, price)



def show_receipt():
    messagebox.showinfo("Receipt", "Receipts "+str(price))


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen

label2 = Label(frame, text="Nights", fg="blue", width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Guests", fg="blue", width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

label4 = Label(frame, text="Cots", fg="blue", width=15, font=("arial", 10, "bold"))   #
label4.grid(row=2, column=0, sticky=W+E)

list1 = ["1", "2", "3", "4"]
guestVar = StringVar()
combo1 = OptionMenu(frame, guestVar, *list1)
guestVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)

cotsVar = StringVar()
combo2 = OptionMenu(frame, cotsVar, *list1)
cotsVar.set("0")
combo2.grid(row=2, column=1, sticky=W+E)

var_cb1 = IntVar()
cb1 = Checkbutton(frame, text="Breakfast", variable=var_cb1)
cb1.grid(row=3, column=0, columnspan=2)

var_cb2 = IntVar()
cb2 = Checkbutton(frame, text="Dinner", variable=var_cb2)
cb2.grid(row=4, column=0, columnspan=2)

button2 = Button(frame, text="GetPrice", fg="black", font=("arial", 10, "bold"), command=get_price)
button2.grid(row=5, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '1')
entry3.grid(row=5, column=1, sticky=W+E)

button3 = Button(frame, text="Receipt", fg="black", font=("arial", 10, "bold"), command=show_receipt)
button3.grid(row=6, column=0, sticky=W+E)


mainloop()
