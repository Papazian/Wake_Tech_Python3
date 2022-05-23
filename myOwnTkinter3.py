from tkinter import *
import tkinter.messagebox as mBox

def showDialog():
	if myOperation.get() == "A":
		mBox.showinfo(message=int(firstNumberTextbox.get())+int(secondNumberTextbox.get()))
	if myOperation.get() == "S":
		mBox.showinfo(message=int(firstNumberTextbox.get())-int(secondNumberTextbox.get()))
	if myOperation.get() == "M":
		mBox.showinfo(message=int(firstNumberTextbox.get())*int(secondNumberTextbox.get()))

myWindow = Tk()

firstNumberLabel = Label(myWindow, text="First Number:")
firstNumberLabel.pack(anchor="w", padx=10, pady=(10,0))	

firstNumberTextbox = Entry(myWindow, width=20)
firstNumberTextbox.pack(anchor="w", padx=10)

secondNumberLabel = Label(myWindow, text="Second Number:")
secondNumberLabel.pack(anchor="w", padx=10, pady=(10,0))	

secondNumberTextbox = Entry(myWindow, width=20)
secondNumberTextbox.pack(anchor="w", padx=10)


myOperation = StringVar()

radioButton1 = Radiobutton(myWindow, text="Addition", variable=myOperation, value="A")
radioButton2 = Radiobutton(myWindow, text="Subtraction", variable=myOperation, value="S")
radioButton3 = Radiobutton(myWindow, text="Multiplication", variable=myOperation, value="M")

radioButton1.select()
radioButton1.pack(anchor="w", padx=10,pady=(10,0))
radioButton2.pack(anchor="w", padx=10,pady=(10,0))
radioButton3.pack(anchor="w", padx=10,pady=(10,0))

myButton = Button(myWindow, text="Calculate", width=20, command=showDialog)
myButton.pack(padx=10, pady=10)

myWindow.mainloop()