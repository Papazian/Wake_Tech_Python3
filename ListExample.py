# define a list a.k.a. an "array" or "vector" in Python
listExample = [0, 1, 2, 3, 4,5, 6]

# reference item #2 in list
print(listExample[2])

# define list of a list
listmatrix = [[0, 1, 2], [3, 4, 5]]
print(listmatrix[1][1])		# the value of 4 in matrix

# define a data table
nameOfColumns = ["Gender","Age"]
listTable = ["F", "5"]

# list with a negative reference
listNames = ["Avery","Bob","Charlie"]
print(listNames[-1])

# use modulus operator to overcome a potential pitfall
# print(listNames[60])
print(listNames[60 % len(listNames)])

# use slice notation to print "Avery" and "Bob"
print(listNames[0:2])

# sets are "unordered" lists that does NOT allow duplicate items
setFruit = {"Apple", "Banana", "Orange", "Apple"}	
print(setFruit)

# dictionaries are like sets (i.e. unordered lists) with "primary keys"
dictExample = {"dayOne":"Monday", "dayTwo":"Tuesday", "dayThree":"Wednesday"}
print(dictExample)
dictBank = {"Avery":0, "Bob":60}
print(dictBank["Avery"]) # identify the primary key
dictBank["Zeb"] = 70
print(dictBank["Zeb"])	# identify the primary key

# print out all keys and values in dictionaries
print(dictBank.keys())
print(dictBank.values())


