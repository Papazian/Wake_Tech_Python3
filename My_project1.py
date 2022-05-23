
# Description: manages bank accounts
# Date: 2/13/2016

# create three independent accounts stored in a dictionary
dictBank = {"John":0, "Donald":0, "Hilary":0}

# define metadata i.e. dictionary to reference inside the previous dictionary
dictMeta = {"1":"John", "2":"Donald", "3":"Hilary"}

# use while loop to continuously display the menu
while True:

	# print the first menu
	print("\nWelcome to the Python baning application!")
	print("What would you like to do?\n")
	print("1. Manage John's account")
	print("2. Manage Donald's account")
	print("3. Manage Hilary's account")
	print("4. View the balance of all accounts")
	print("5. Exit")

	# retrieve user input from first menu
	userInput = int(input("Please enter choice: "))
	
	# check if user wants to manage a specific account
	if (userInput in [1,2,3]):
	
		# print the second menu
		print("\nWhat would you like to do with ",dictMeta[str(userInput)],"'s account?")
		print("1. Deposit")
		print("2. Withdraw")
		print("3. Check Balance")
		
		# retrieve user input from second menu
		transactionInput = int(input("Please enter choice: "))
		
		# deposit into bank account
		if (transactionInput==1):
			deposit = float(input("How much would you like to deposit? "))
			dictBank[dictMeta[str(userInput)]] += deposit
			print(dictMeta[str(userInput)],"'s new account balance is ",dictBank[dictMeta[str(userInput)]])

		# withdraw from bank account
		elif (transactionInput==2):
			withdraw = float(input("How much would you like to withdraw? "))
			
			# before proceeding, check to ensure we do not over-draw from account
			if ((dictBank[dictMeta[str(userInput)]]-withdraw) >= 0):
				dictBank[dictMeta[str(userInput)]] -= withdraw
				print(dictMeta[str(userInput)],"'s new account balance is ",dictBank[dictMeta[str(userInput)]])

			# display error if the user attempts to over-draw from account
			else:
				print("\nError: that amount would over-draw the account!")

		# check the current account balance		
		elif (transactionInput==3):
			print(dictMeta[str(userInput)],"'s current account balance is ",dictBank[dictMeta[str(userInput)]])
		
		# warn user of invalid input for second menu
		else: 
			print("\nYour input was not valid.")
			
	# use for loop to view the account balance of all accounts
	elif (userInput==4):
		for key in dictMeta:
			print(dictMeta[key],"'s current account balance is ",dictBank[dictMeta[key]])
			
	# have ability to exit the program using the break keyword
	elif (userInput==5):
		break
		
	# warn user of invalid input for first menu
	else:
		print("\nYour input was not valid. Please try again")



			


