from BankAccount import *	# required for object oriented classes in Python

accountOne = BankAccount(0, "Avery")

print("Initial balance is",accountOne.getBalance())

depositAmount = int(input("Please enter a deposit amount: "))
accountOne.deposit(depositAmount)

print("Balance after deposit is",accountOne.getBalance())

withdrawAmount = int(input("Please enter a withdraw amount: "))
accountOne.withdraw(withdrawAmount)

print("Balance after withdraw is",accountOne.getBalance())

accountTwo = BankAccount(0, "Leonardo")
print("The number of bank accounts:",BankAccount.count)

