class Animal:

	def __init__(self, name):
		self.name = name
		
	def talk(self):
		return "I don't know what I am"
	
	
class Cat(Animal):		# child class Cat inherits from parent class Animal

	def talk(self):		# override the talk() method
		return "Meow!"
		

class Dog(Animal):

	def talk(self):
		return "Woof!"
		
		
class Fox(Animal):		# use the default talk() method of the base class here

	def doNothing(self):
		pass
		
		
animals = [Cat("Alpha Kitten"),Dog("Beta Doggy"),Fox("Gamma Foxy")]	# declare a list of objects

for ani in animals:
	print(ani.name + ": " + ani.talk())
	
