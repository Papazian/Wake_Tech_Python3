from tkinter import *
import tkinter.messagebox as mBox

def displayMessagebox():
	myNum = myListbox.curselection()[0]
	if (myNum==2):
		mBox.showinfo(title="Selection Information", message=myTextbox.get()+" is an "+myListbox.get(myListbox.curselection()))
	else:
		mBox.showinfo(title="Selection Information", message=myTextbox.get()+" is a "+myListbox.get(myListbox.curselection()))

myWindow = Tk()

nameLabel = Label(myWindow, text="Name:")
nameLabel.pack(padx=10, pady=(10,0))	

myTextbox = Entry(myWindow, width=20)
myTextbox.pack(padx=10)

occupationLabel = Label(myWindow, text="Occupation:")
occupationLabel.pack(padx=10, pady=(10,0))	

myListbox = Listbox(myWindow)
myListbox.insert(1,"Scientist")
myListbox.insert(2,"Programmer")
myListbox.insert(3,"Accountant")
myListbox.insert(4,"Historian")
myListbox.insert(5,"Salesman")
myListbox.pack(padx=10)
myListbox.selection_set(0)

myButton = Button(myWindow, text="Choose", width=20, command=displayMessagebox)
myButton.pack(padx=10, pady=10)

myTextbox.focus()	# puts the focus on the textbox

myWindow.mainloop()

