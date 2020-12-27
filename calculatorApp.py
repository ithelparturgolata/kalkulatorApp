import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("240x360")
root.resizable(0,0)

operator = ""
textInput = StringVar()

def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)

def buttonClearDisplay():
    global operator
    operator = ""
    textInput.set("")

def buttonEquals():
    global operator
    total = str(eval(operator))
    textInput.set(total)
    operator = "" 

#app Frame root
appMain = Frame(root, pady=20)
appFirstColumn = Frame(root,pady=20)
appSecondColumn = Frame(root, pady=20)
appThirdColumn = Frame(root, pady=20)
appFourthColumn = Frame(root, pady=20)

#app Grid
appMain.grid(row=0, column=0, columnspan=3)
appFirstColumn.grid(row=1, column=0)
appSecondColumn.grid(row=1, column=1)
appThirdColumn.grid(row=1, column=2)
appFourthColumn.grid(row=1, column=3)

#widget appMain
EntryResultDisplay = Entry(appMain, width=15, font=("bold", 20), textvariable=textInput, justify="right")
EntryResultDisplay.grid(row=0, column=0, columnspan=3, padx=2, pady=2)

#widget appFirstColumn

button7 = Button(appFirstColumn, text="7", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(7))
button7.grid(row=1, column=0, padx=2, pady=2)

button4 = Button(appFirstColumn, text="4", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(4))
button4.grid(row=2, column=0, padx=2, pady=2)

button1 = Button(appFirstColumn, text="1", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(1))
button1.grid(row=3, column=0, padx=2, pady=2)

buttonC = Button(appFirstColumn, text="C", width=6, height=3, activebackground="yellow", command=lambda:buttonClearDisplay())
buttonC.grid(row=4, column=0, padx=2, pady=2)

#widget appSecondColumn

button8 = Button(appSecondColumn, text="8", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(8))
button8.grid(row=1, column=1, padx=2, pady=2)

button5 = Button(appSecondColumn, text="5", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(5))
button5.grid(row=2, column=1, padx=2, pady=2)

button2 = Button(appSecondColumn, text="2", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(2))
button2.grid(row=3, column=1, padx=2, pady=2)

button0 = Button(appSecondColumn, text="0", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(0))
button0.grid(row=4, column=1, padx=2, pady=2)

#widget appThirdColumn

button9 = Button(appThirdColumn, text="9", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(9))
button9.grid(row=1, column=2, padx=2, pady=2)

button6 = Button(appThirdColumn, text="6", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(6))
button6.grid(row=2, column=2, padx=2, pady=2)

button3 = Button(appThirdColumn, text="3", width=6, height=3, activebackground="yellow", command=lambda:buttonClick(3))
button3.grid(row=3, column=2, padx=2, pady=2)

buttonEqual = Button(appThirdColumn, text="=", width=6, height=3, activebackground="yellow", command=buttonEquals)
buttonEqual.grid(row=4, column=2, padx=2, pady=2)

#widget appFourthColumn

buttonPlus = Button(appThirdColumn, text="+", width=6, height=3, activebackground="yellow", command=lambda:buttonClick("+"))
buttonPlus.grid(row=1, column=3, padx=2, pady=2)

buttonMinus = Button(appThirdColumn, text="-", width=6, height=3, activebackground="yellow", command=lambda:buttonClick("-"))
buttonMinus.grid(row=2, column=3, padx=2, pady=2)

buttonMultiply = Button(appThirdColumn, text="*", width=6, height=3, activebackground="yellow", command=lambda:buttonClick("*"))
buttonMultiply.grid(row=3, column=3, padx=2, pady=2)

buttonDivision = Button(appThirdColumn, text="/", width=6, height=3, activebackground="yellow", command=lambda:buttonClick("/"))
buttonDivision.grid(row=4, column=3, padx=2, pady=2)


root.mainloop()