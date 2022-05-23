class BankAccount:

	count = 0

	def __init__(self, initialBalance, name):
		self.balance = initialBalance
		self.owner = name
		BankAccount.count += 1
		
	def deposit(self, amount):
		self.balance += amount
		
	def withdraw(self, amount):
		self.balance -= amount
		
	def getBalance(self):
		return self.balance


# Four Principles of Object-Oriented Programming:
# 1) Encapsulation
# 2) Data Abstraction
# 3) Polymorphism
# 4) Inheritance

