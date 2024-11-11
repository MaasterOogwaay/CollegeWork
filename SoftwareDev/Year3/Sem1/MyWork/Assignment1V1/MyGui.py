from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x850")
window.title("Welcome")


#______________________________________________
from MyDecTreeHealth import MyDecisionTreeHealth


decisionTree = MyDecisionTreeHealth()
def trainData():
    newSeedValue = int(seedsVar.get())
    decisionTree.updateSeed(newSeedValue)
    decisionTree.trainData()

def testData():
    text.delete("1.0","end")    # Clear the Text Area

    text.insert(END, decisionTree.readCategories())
    result, accuracy = decisionTree.testData()
    text.insert(END, '\n['+str(result[0]))
    text.insert(END, '\n '+str(result[1]))
    text.insert(END, '\n '+str(result[2]) +']')

    text.insert(END, '\n\nAccuracy ' + str(int(accuracy*100)) + '%')
def makeNewPrediction():

    relwt = float(entry42.get())
    glufast = int(entry43.get())
    glutest = int(entry44.get())
    instest = int(entry44a.get())
    sspg = int(entry44b.get())

    prediction_Res = decisionTree.makePrediction(relwt, glufast, glutest, instest, sspg)
    result = 'Normal'
    if prediction_Res == 'Chemical_Diabetic':
        result = 'Chemical Diabetic'
    if prediction_Res == 'Overt_Diabetic':
        result = 'Overt Diabetic'
    entry45.delete(0, END)
    entry45.insert(END, result)




frame = Frame(window, width=450, height=450)
frame.place(x=10, y=100)
label0 = Label(window, text="Diabetes Predictor", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label0.place(x=90, y=30)                            # place on screen

label01 = Label(window, text="First Enter Seed Value for Random No Generator", fg="red", font=("arial", 11, "bold"))
label01.place(x=5, y=70)


label1 = Label(frame, text="      Enter Seed Value     ", fg="blue", width=15, font=("arial", 10, "bold"))   #
label1.grid(row=0, column=0, sticky=W+E)

list1 = ['1', '2', '3', '4', '5']
seedsVar = StringVar()
combo1 = OptionMenu(frame, seedsVar, *list1)
seedsVar.set("1")
combo1.grid(row=0, column=1, sticky=W+E)

button1 = Button(frame, text="     Train Data    ", fg="black", font=("arial", 10, "bold"), command=trainData)
button1.grid(row=1, column=0, sticky=W+E)

button2 = Button(frame, text="     Test Data      ", fg="black", font=("arial", 10, "bold"), command=testData)
button2.grid(row=1, column=1, sticky=W+E)

label3 = Label(frame, text="Output", fg="blue", width=15, font=("arial", 10, "bold"))   #
label3.grid(row=2, column=0)


text = Text(frame, height=6, width=7)
text.grid(row=2, column=1, ipadx=100)

label02 = Label(frame, text="      ", fg="red", font=("arial", 16, "bold"))
label02.grid(row=3, column=0, columnspan=2, sticky=W+E)

label03 = Label(frame, text="Now Test for New Data", fg="red", font=("arial", 14, "bold"))
label03.grid(row=4, column=0, columnspan=2,sticky=W+E)

label42 = Label(frame, text="Relative Weight", fg="blue", width=15, font=("arial", 10, "bold"))   #
label42.grid(row=6, column=0, sticky=W+E)
entry42 = Entry(frame)
entry42.insert(END, '')
entry42.grid(row=6, column=1, sticky=W+E)

label43 = Label(frame, text="Fasting Plasma", fg="blue", width=15, font=("arial", 10, "bold"))   #
label43.grid(row=7, column=0, sticky=W+E)
entry43 = Entry(frame)
entry43.insert(END, '')
entry43.grid(row=7, column=1, sticky=W+E)

label44 = Label(frame, text="Plasma Glucose Level", fg="blue", width=15, font=("arial", 8, "bold"))   #
label44.grid(row=8, column=0, sticky=W+E)
entry44 = Entry(frame)
entry44.insert(END, '')
entry44.grid(row=8, column=1, sticky=W+E)

label44a = Label(frame, text="Plasma Insulin", fg="blue", width=15, font=("arial", 10, "bold"))   #
label44a.grid(row=9, column=0, sticky=W+E)
entry44a = Entry(frame)
entry44a.insert(END, '')
entry44a.grid(row=9, column=1, sticky=W+E)

label44b = Label(frame, text="Steady Plasma Glucose", fg="blue", width=15, font=("arial", 8, "bold"))   #
label44b.grid(row=10, column=0, sticky=W+E)
entry44b = Entry(frame)
entry44b.insert(END, '')
entry44b.grid(row=10, column=1, sticky=W+E)

button3 = Button(frame, text="Make Prediction", fg="black", font=("arial", 10, "bold"), command=makeNewPrediction)
button3.grid(row=11, column=0, sticky=W+E)
entry45 = Entry(frame)
entry45.insert(END, '')
entry45.grid(row=11, column=1, sticky=W+E)

#canvas = Canvas(window, width = 390, height = 390)
#canvas.place(x=1,y=460)


#image = PhotoImage(file="TestIris1.png")

#canvas.create_image(1,1,  anchor='nw', image=image)
label02a = Label(frame, text="      ", fg="red", font=("arial", 16, "bold"))
label02a.grid(row=12, column=0, columnspan=2,sticky=W+E)
label03b = Label(frame, text="Diabetic Type Evaluation", fg="red", font=("arial", 14, "bold"))
label03b.grid(row=13, column=0, columnspan=2,sticky=W+E)

textb = Text(frame, height = 10, width = 12 )
textb.grid(row=14, column=0, columnspan=2,ipadx=100)
textb.insert(END, '\nDistinguishing between the three clinical groups is very simple')
textb.insert(END, '\n')
textb.insert(END, '\nPlasma Glucose Level < 420 = Normal')
textb.insert(END, '\nFasting Plasma Gluscose < 117 = Chemical Diabetic')
textb.insert(END, '\nFasting Plasma Gluscose > 117 = Overt Diabetic')

mainloop()