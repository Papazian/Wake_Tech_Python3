
# Description: Authenticate users when they attempt to gain access to a system
# Date: 2/27/2016



# Define function to encrypt text into a coded message using a Caesar Cipher of 1
def encrypt(text):
	code=""									# Default encrypted message is empty
	for i in text:							# Loops through each character in text string
		code += chr(ord(i)+1)				# The encrypted character is the character value of the (ASCII number + 1)
	return(code)							# Return the encrypted code
	
# Define function to decrypt code into a text string using the Reverse of the Caesar Cipher of 1
def decrypt(code):
	text=""									# Default decrypted text string is empty
	for i in code:							# Loops through each character in encrypted code
		text += chr(ord(i)-1)				# The decrypted character is character value of the (ASCII number - 1)
	return(text)							# Return the text message

# Define function to return true if the name contains only letters and numbers and contains at least one capital letter
def isValidUsername(checkName):
	return ((checkName.lower() != checkName) and checkName.isalnum())	

# Define function to open file for reading, check each line for login name, then return boolean value
def isUsername(loginName):
	myFile = open("usernames.txt", "r")		# Opens file for reading
	loginNameInFile = False					# Default boolean value is that login name is not in file
	for line in myFile:						# Loops through every line in file
		if (line.strip("\n") == encrypt(loginName)):
			loginNameInFile = True			# If the encrypted login name is a line in file, then change the boolean value
	myFile.close()							# Closes file
	return loginNameInFile					# Return the boolean value

# Define function to open file for appending, add new encrypted username, and then close file
def addUsername(newName):
	myFile = open("usernames.txt", "a")		# Opens file for appending
	myFile.write(encrypt(newName) + "\n")	# Appends file with new username encrypted
	myFile.close()							# Closes file

# Define function to show all accounts
def showAllAccounts():
	myFile = open("usernames.txt", "r")		# Opens file for reading
	for line in myFile:						# Loops through every encrypted login name in file
		print(decrypt(line.strip("\n")))	# Prints each decrypted login name 
	myFile.close()							# Closes file



# Before the main menu loop begins, make sure that a file exists	
try:
    myFile = open("usernames.txt", "r")		# Try to open a pre-existing file of usernames
except (FileNotFoundError):
	myFile = open("usernames.txt", "w")		# Create a new file if the file doesn't already exist
finally:
    myFile.close()
	
# use while loop to continuously display the menu
while True:

	# Print the main menu
	print("\nWhat would you like to do?\n")
	print("1. Authenticate")
	print("2. Create a New Account")
	print("3. Show all Accounts")
	print("4. Exit")

	# Try to retrieve an integer input from main menu
	try:
		userChoice = int(input("Please enter choice: "))
		
		# Authenticate user
		if (userChoice == 1):
			inputName = input("\nPlease type your username: ")
			if (isUsername(inputName)):		# Determine if the input is a registered username in the file
				print("Access Approved!\n")
				break						# If authenticated, then exit program
			else:
				print("Access Denied!")		# Otherwise, give the user another chance
			
		# Create a new account
		elif (userChoice == 2):
			notAddedNameYet = True			# Set default boolean value that new username has not been added yet
			while notAddedNameYet:			# Loop until a new account is created
				inputName = input("\nPlease type a new username: ")
				if (isValidUsername(inputName)):	# First, check if the input is a valid username, and then continue
					if (isUsername(inputName)):			# Check if the username already exists in the file
						print("Sorry - that username has already been taken and it exists in the file")
					else:
						addUsername(inputName)			# If the username does not already exist in file, then add it to file
						notAddedNameYet = False			# Change the boolean value to exit loop
				else:								# Otherwise, since the input is an invalid, give the user another chance
					print("Sorry - you can only use letters and numbers")
					print("and the new username must contain at least one capital letter!")
			
		# Show all usernames
		elif (userChoice == 3):
			showAllAccounts()
		
		# Exit the program
		elif (userChoice == 4):
			break
			
		# Otherwise, give the user another chance to enter choice
		else:
			print("Sorry - you must enter either 1, 2, 3, or 4")
			
	except Exception as msg:	# The keyword "Exception" captures every possible error
		print("Sorry - you must enter either 1, 2, 3, or 4")	# Give the user another chance to enter choice


