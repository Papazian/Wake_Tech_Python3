	
def factorial(n):
	if n>0:
		return (n*factorial(n-1))
	else:
		return 1
	
n = int(input("What is your number n: "))

print("when n =",n," factorial(n) =",factorial(n))

