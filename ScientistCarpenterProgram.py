from ScientistCarpenterClass import *

def describe(object):
	print(object.getDescription())
	print(object.getTools())
	
myScientist = Scientist()
myCarpenter = Carpenter()

describe(myScientist)
describe(myCarpenter)

