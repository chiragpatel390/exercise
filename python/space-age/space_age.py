def operation(time):
	def op(self):
		return round(self.seconds/time,2)
	return op

class SpaceAge(object):
	def __init__(self, seconds):
		self.seconds=seconds

	on_earth = operation(31557600)
	on_mercury = operation(31557600*0.2408467)
	on_venus = operation(31557600*0.61519726)
	on_mars = operation(31557600*1.8808158)
	on_jupiter = operation(31557600*11.862615)
	on_saturn = operation(31557600*29.447498)
	on_uranus = operation(31557600*84.016846)
	on_neptune = operation(31557600*164.79132)