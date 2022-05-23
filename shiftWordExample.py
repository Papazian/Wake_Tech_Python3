def shiftWordByTwo(word):
	newWord = word[2:] + word[:2]
	return newWord

#inputWord = input("Please enter a word: ")
#shiftedWord = shiftWordByTwo(inputWord)
#print("You shifted word is: ", shiftedWord)

def isPalindrome(word):
	return (word.lower() == word[::-1].lower())
	
inputWord = input("Please enter a word: ")
result = isPalindrome(inputWord)
if result:
	print(result, " is a palindrone")
else:
	print(result, " is NOT a palindron")
	
	
# Python string website: https://docs.python.org/2/library/string.html 

# "{0}(1}(0}".format("abra","cad")
# "{:,}".format(total)

