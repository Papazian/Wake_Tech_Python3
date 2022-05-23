myFile = open("testFile.txt", "w")	# creates a file if it does not exist

myFile.write("Hello World\n")
myFile.write("Second line\n")

myFile.close()

newFile = open("testfile.txt", "r")	# opens a file that must already exist

for line in newFile:
	print(line,end="")

newFile.close()


##############


with open("testFile2.txt", "w") as file:
	file.write("John\n")
	file.write("Robert\n")
	file.write("Betsy\n")
	
with open("testFile2.txt", "r") as file:
	for line in file:
		print(line, end="")


##############


def writeLineWithSep(file, line):
	file.write(line + "\n")

with open("testFile3.txt", "w") as file:
	writeLineWithSep(file, "Blue")
	writeLineWithSep(file, "Red")
	writeLineWithSep(file, "Green")


##############


string = "This is"

with open("testFile4.txt", "w") as file:	# creates a file if it does not exist
	print("File pointer: ", file.tell())
	file.write(string)
	print("File pointer: ", file.tell())

print("\nDone writing the string\n")

with open("testFile4.txt", "r+") as file:	# reading and writing
	print("File pointer: ", file.tell())
	print("File string: ", file.read())
	print("File pointer: ", file.tell())

print("\nDone reading the string\n")

with open("testFile4.txt", "r+") as file:
	file.seek(7)
	file.write(" a string")
	file.seek(0)
	print("File String:", file.read())
	 
	file.seek(7)
	file.write(" at the beginnning of the file")
	file.seek(0)
	print("File string:", file.read())
	


	
	


		