number = int(input("Please enter a number: "))

# in Python, spacing matters a lot unlike other languages
# the tab indicates a "code block"
if number > 100:
	print("The number is too high")
	print("line2")
	print("line3")
elif number < 100:
	print("The number is too low")
else:
	print("The number is just right!")
	
# the if-then block ends with a statement outside of the tab "code block"
print("Now we are outside the code block")

