
try:
	#num = 1/0
	a = int(input("Please enter a number: "))
	
except Exception as msg:	# the keyword "Exception" capture every possible error
	print("ERROR:", msg)
	



	
day = 32

try:
	if day > 31:
		raise ValueError("Invalid Day Number")
except Exception as msg:
	print("ERROR:", msg)
finally:
	print("But I'm having fun anyway")

	