myFile = open("testFile5.txt", "w")	

for x in range(1, 3):
	myLine = input("Please enter a line of text: ")
	myFile.write(myLine + "\n")

myFile.close()
 
mySearch = input("Search for what text? ")

myFile = open("testFile5.txt", "r")	

existsSearchInFile = False

for line in myFile:
	if (line.strip("\n") == mySearch):
		existsSearchInFile = True

if (existsSearchInFile):
	print("Yes, the search text is in the file")
else:
	print("Nope, the search text is NOT in the file")

myFile.close()

