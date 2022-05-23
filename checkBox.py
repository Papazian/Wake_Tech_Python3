from tkinter import *
import tkinter.messagebox as mBox

def displayDialog():
	messageString = "Your favorite colors are: "
	if var_checkButton1.get() == 1:
		messageString += "\nRed"
	if var_checkButton2.get() == 1:
		messageString += "\nBlue"	
	if var_checkButton3.get() == 1:
		messageString += "\nGreen"
	mBox.showinfo(title="Favorite Colors", message=messageString)

	
myWindow = Tk()

var_checkButton1 = IntVar()
var_checkButton2 = IntVar()
var_checkButton3 = IntVar()

checkButton1 = Checkbutton(myWindow,variable=var_checkButton1,
							text="Red", onvalue=1, offvalue=0)
checkButton2 = Checkbutton(myWindow,variable=var_checkButton2,
							text="Blue", onvalue=1, offvalue=0)
checkButton3 = Checkbutton(myWindow,variable=var_checkButton3,
							text="Green", onvalue=1, offvalue=0)

# use anchor to anchor check buttons to the West for left justified formatting
checkButton1.pack(anchor="w", padx=10,pady=(10,0))
checkButton2.pack(anchor="w", padx=10,pady=(10,0))
checkButton3.pack(anchor="w", padx=10,pady=(10,0))
	
myButton = Button(myWindow, text="Select Colors", command=displayDialog)
myButton.pack(padx=10, pady=10)	
	
myWindow.mainloop()