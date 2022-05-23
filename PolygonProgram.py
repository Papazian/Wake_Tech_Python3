from Polygon import *


class Rectangle(Polygon):	# child class Rectangle inherits properties and methods from Polygon paraent class

	# No constructor function __init__() is required beacuse we have a constructor in the parent class
	
	def area(self):
		return(self.width * self.height)
		
	def whatAmI(self):		# overrides the method in the parent class
		print("I am a rectange")
		

class Triangle(Polygon):
		
	def area(self):
		return((self.width * self.height)/2)
		
	def whatAmI(self):		# overrides the method in the parent class
		print("I am a triangle")
			
	
rect = Rectangle(4, 5)
tri = Triangle(4, 5)

print("Rectange Area:", rect.area())
print("Triangle Area:", tri.area())

rect.whatAmI()
tri.whatAmI()

