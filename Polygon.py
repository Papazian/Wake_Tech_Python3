class Polygon:
	
	count = 0
	
	def __init__(self, height, width):
		self.height = height
		self.width = width
		Polygon.count += 1
		
	def whatAmI(self):
		print("I am a Polygon")
		
