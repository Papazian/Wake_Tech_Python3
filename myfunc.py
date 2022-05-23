def printHelloWorld():
	global b	# globalizes a local variable
	b = 10
	print("Hello World")

printHelloWorld()

	
globalVariable = 1

def printVariable(number):
	print("Global Variable:", globalVariable)
	number += 5
	
	localVariable = 2
	print("Local Variable:", localVariable)
	
	global coercedGlobal
	coercedGlobal = 3
	
printVariable(4)
print("Coerced Global:", coercedGlobal)


