from tkinter import *
import tkinter.messagebox as mBox

def showDialog():
	mBox.showinfo("Selection",animal.get())

myWindow = Tk()

animal = StringVar()

radioButton1 = Radiobutton(myWindow, text="Fish", variable=animal, value="These creatures live in the ocean")
radioButton2 = Radiobutton(myWindow, text="Mammals", variable=animal, value="These creatures live on land")
radioButton3 = Radiobutton(myWindow, text="Birds", variable=animal, value="These creatures live in the air")

radioButton1.select()
radioButton1.pack()
radioButton2.pack()
radioButton3.pack()

myButton = Button(myWindow, text="Where do they live?", command=showDialog)
myButton.pack()

myWindow.mainloop()