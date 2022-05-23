def equalsIsIgnoreCase(stringOne, stringTwo):
	return (stringOne.upper() == stringTwo.upper())
	
stringOneInput = input("Please enter a first string: ")
stringTwoInput = input("Please enter a second string: ")

result = equalsIsIgnoreCase(stringOneInput, stringTwoInput)

if result:
	print("They are equal ignoring case")
else:
	print("They are NOT equal ignoring case")
	
