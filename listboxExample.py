from tkinter import *
import tkinter.messagebox as mBox

def displayMessagebox():
	mBox.showinfo(title="Selection Information", 
				  message="You chose "+myListbox.get(myListbox.curselection()))

myWindow = Tk()

myListbox = Listbox(myWindow)
myListbox.insert(1,"John Papazian")
myListbox.insert(2,"Betsy Matthews")
myListbox.insert(3,"Robert Moriera")

myListbox.pack(padx=10, pady=10)

myButton = Button(myWindow, text="Choose", command=displayMessagebox)
myButton.pack(padx=10, pady=10)

myWindow.mainloop()

