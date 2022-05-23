#looping menu
while True:
	userInput = int(input("\n\nWhat would you like to do?\n 1. Add two numbers\n 2. Subtract two numbers\n 3. Exit\n"))
	if (userInput==1):
		number1 = int(input("\nPlease enter the first number: "))
		number2 = int(input("\nPlease enter the second number: "))
		print("\nThe result is",number1+number2)
	elif (userInput==2):
		number1 = int(input("\nPlease enter the first number: "))
		number2 = int(input("\nPlease enter the second number: "))
		print("\nThe result is",number1-number2)
	elif (userInput==3):
		break
	else:
		print("\nYour input is not valid. Please enter 1, 2, or 3")

		
