EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.bearing = bearing
		self.x = x
		self.y = y
		self.coordinates = (self.x,self.y)

	def turn_right(self):
		if self.bearing==0:
			self.bearing=3
		elif self.bearing==1:
			self.bearing=0
		elif self.bearing==2:
			self.bearing=1
		elif self.bearing==3:
			self.bearing=2

	def turn_left(self):
		if self.bearing==0:
			self.bearing=1
		elif self.bearing==1:
			self.bearing=2
		elif self.bearing==2:
			self.bearing=3
		elif self.bearing==3:
			self.bearing=0

	def advance(self):
		if self.bearing==0:
			self.x+=1
		elif self.bearing==1:
			self.y+=1
		elif self.bearing==2:
			self.x-=1
		elif self.bearing==3:
			self.y-=1
		self.coordinates=(self.x,self.y)

	def simulate(self,action):
		for i in range(len(action)):
			if action[i]=='A':
				self.advance()
			elif action[i]=='L':
				self.turn_left()
			elif action[i]=='R':
				self.turn_right()