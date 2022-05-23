from tkinter import *

# functions should always be at the top of the code

def changeBackground():
	myWindow.configure(background="black")

myWindow = Tk()	# display at the stop
myWindow.geometry("400x100")
myWindow.title("Hello World Program")

myLabel = Label(myWindow, text="Hello World!", font=("Times New Roman",16))
myLabel.place(x=140,y=20)

myButton = Button(myWindow, text="Exit", height=1, width=17, command=exit)
myButton.place(x=140,y=75)

myOtherButton = Button(myWindow, text="Change Background Color", command=changeBackground)
myOtherButton.place(x=130,y=50)

myWindow.mainloop()	# display at the end