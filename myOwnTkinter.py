from tkinter import *

# functions should always be at the top of the code

myCount = 0;

def changeLabel():
	global myCount
	if (myCount==0):
		myLabel.configure(text="The button has been pushed!")
		myCount = myCount+1
	else:
		myLabel.configure(text="Please push the botton")
		myCount = myCount-1

myWindow = Tk()	# display at the stop
# myWindow.geometry("400x100")
myWindow.title("Hello World Program")	# default window size based upon packing

myLabel = Label(myWindow, text="Please push the botton", font=("Times New Roman",16))
# myLabel.place(x=140,y=20)
myLabel.pack()	# default location

myButton = Button(myWindow, text="Change Label", command=changeLabel)
# myButton.place(x=130,y=50)
myButton.pack()

myWindow.mainloop()	# display at the end