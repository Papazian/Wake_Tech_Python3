import planet	# import the "planet" module

# alternative method to import without needing planet.method() nomenclature
from planet import bestPlanet, worstPlanet, isEarth 

planet.bestPlanet()
planet.worstPlanet()
planet.isEarth()
planet.bestPlanet("Mars")
planet.worstPlanet("Mars")
planet.isEarth("Earth")

