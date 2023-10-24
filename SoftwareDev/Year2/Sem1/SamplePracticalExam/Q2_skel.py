

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("List Functions")


def allBetween(list, low, high):
    result = True
    for el in list:
        if el < low or el > high:
            result = False
    return result


def addBetween(list, low, high):
    result = 0
    for el in list:
        if el >= low and el <= high:
            result += el
    return result


def searchEvent():
    global list1
    low = int(entry3.get())
    high = int(entry4.get())
    result = allBetween(list1,low,high)
    entry5.delete(0, END)
    if result == True:
        entry5.insert(END, 'True')
    else:
        entry5.insert(END, 'False')


def addEvent():
    global list1
    low = int(entry3.get())
    high = int(entry4.get())
    result = addBetween(list1, low, high)
    entry6.delete(0, END)
    entry6.insert(END, result)


list1 = [2, 6, 2, 7, 8, 4, 2, 6]
label1 = Label(window, text="List Functions", fg="blue", bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen

label2 = Label(window, text="Value1", fg="blue", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '[2, 6, 2, 7, 8, 4, 2, 6]')
entry2.place(x=130, y=80)

label3 = Label(window, text="Lower Limit", fg="blue", width=10, font=("arial", 12, "bold"))   #
label3.place(x=10, y=120)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=130, y=120)

label4 = Label(window, text="Upper Limit", fg="blue", width=10, font=("arial", 12, "bold"))   #
label4.place(x=10, y=160)

entry4 = Entry(window)
entry4.insert(END, '10')
entry4.place(x=130, y=160)


button1 = Button(window, text="allBetween", width=16, fg="black", font=("arial", 10, "bold"), command=searchEvent)
button1.place(x=20, y=200)

entry5 = Entry(window, width=13)
entry5.insert(END, '')
entry5.place(x=180, y=200)

button2 = Button(window, text="add Between Limits", width=16, fg="black", font=("arial", 10, "bold"), command=addEvent)
button2.place(x=20, y=240)

entry6 = Entry(window, width=13)
entry6.insert(END, '1')
entry6.place(x=180, y=240)


mainloop()
