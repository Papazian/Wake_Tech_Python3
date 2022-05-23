def countSpaces(word):
	return word.count(" ")
	
def hasAtLeastOneCap(word):
	return not(word.islower())

def hasAtLeastOneCap2(word):
	return word.lower() != word
	
#print("The number of spaces: ", countSpaces(inputWord))
	

myEval = True

inputWord = input("Please enter a string: ")
myEval = hasAtLeastOneCap(inputWord)

while not(myEval):
	inputWord = input("Please enter a string: ")
	myEval = hasAtLeastOneCap(inputWord)
	
print(inputWord, " has at least one capital letter")
