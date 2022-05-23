from tkinter import *
import tkinter.messagebox as mBox	# renames class

def displayMessage():
	# mBox.showinfo(title="Greetings!",message="Hey "+myTextbox.get())
	result = mBox.askyesno(title="Greetings!",message="Would you like a greeting?")
	if result == 1:
		mBox.showinfo(title="Greetings!",message="Hey "+myTextbox.get())

myWindow = Tk()

myTextbox = Entry(myWindow)
myTextbox.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(myWindow, text="Greet Me!",command=displayMessage)
myButton.grid(row=0, column=1, padx=10, pady=10)

myWindow.mainloop()

