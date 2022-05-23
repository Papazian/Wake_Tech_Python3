class Vehicle:

	def __init__(self, gasMlg, remaining):	# Methods with double underscores are Private!
		self.__milage__ = gasMlg			# Properties with double underscores are Private!
		self.__gasRemaining__ = remaining
	
	def drive(self, distance):
		longestDistance = self.__gasRemaining__ * self.__milage__
		if (distance > longestDistance):
			return "You can't travel that far"
		else:
			return "You can make it!"
			
	def setMileage(self, gasMlg):
		self.__milage__ = gasMlg
		
	def getMileage(self):
		return self.__milage__
		
