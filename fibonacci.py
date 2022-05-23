
def fibonacci(n):
	if (n>1):
		return(fibonacci(n-1)+fibonacci(n-2))
	elif (n==1):
		return 1
	else:
		return 0
	
	
n = int(input("What is your number n: "))

print("when n =",n," fibonacci(n) =",fibonacci(n))

