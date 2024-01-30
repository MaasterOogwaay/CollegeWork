

from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

from Ex215MyClasses import *


#------------end of class definition------------------

def display():
    name = a1.getName()
    age = a1.getAge()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, name)
    entry2b.delete(0, END)  # delete old value
    entry2b.insert(END, age)
    year = a1.getYear()
    course = a1.getCourse()
    entry2c.delete(0, END)  # delete old value
    entry2c.insert(END, course)
    entry2d.delete(0, END)  # delete old value
    entry2d.insert(END, year)





def ageEvent():
    a1.stepAge()
    display()

def yearEvent():
    a1.stepYear()
    display()

def courseEvent():
    course = entry4.get()
    a1.updateCourse(course)
    display()

a1=Student("J.Smith",22, "BSc Software", 2);


label1 = Label(window, text="Student Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)

# place on screen
label3 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3b = Label(window, text="Age", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3b.place(x=10, y=110)

entry2b = Entry(window)
entry2b.insert(END, '')
entry2b.place(x=120, y=110)



label3c = Label(window, text="Course", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3c.place(x=10, y=140)

entry2c = Entry(window)
entry2c.insert(END, '1')
entry2c.place(x=120, y=140)

entry2d = Entry(window)
entry2d.insert(END, '10')
entry2d.place(x=120, y=170)

label3d = Label(window, text="studyYear", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3d.place(x=10, y=170)





button4= Button(window, text="stepAge", fg="black", font=("arial", 10, "bold"), command=ageEvent)
button4.place(x=40, y=210)

button4b= Button(window, text="stepYear", fg="black", font=("arial", 10, "bold"), command=yearEvent)
button4b.place(x=120, y=210)



button4= Button(window, text="updateCourse", fg="black", font=("arial", 10, "bold"), command=courseEvent)
button4.place(x=40, y=240)

entry4 = Entry(window)
entry4.insert(END, 'BSc Business')
entry4.place(x=145, y=245)



display()

mainloop()
