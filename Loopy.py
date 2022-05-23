number = 0

# while loops - use tabs to indicate the loop block
while (number < 10):
	print(number)
	number = number + 1
	
# infinite loops when break is off
while True:
	print("Hello")
	break
	
# use the IN operator
a = [0,1,2]

if (2 in a):
	print ("Note that 2 is in a")
	
if (5 not in a):
	print ("Note that 5 is not in a")

# continue in loops	
number = 0
while (number < 10):
	if (number %2 == 0):
		number = number + 1
		continue	# jumps back to start of loop
	number = number + 1
	print(number)

# for loops to iterate X number of times	
for i in range(0, 10):
	print(i)

# continuous loop
programEnds=False
while not programEnds:
	userInput = int(input("Has the programmed ended?"))
	if userInput==1:
		programEnds=True
		


