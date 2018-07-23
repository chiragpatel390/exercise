from string import ascii_uppercase
from random import choice

class Robot(object):
	
	names = []

	def __init__(self):
		name_set=False

		while name_set==False:
			new_name=choice(ascii_uppercase)+choice(ascii_uppercase)+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
			if new_name not in Robot.names:
				self.name=new_name
				Robot.names.append(new_name)
				name_set=True

	def reset(self):
		name_set=False

		while name_set==False:
			new_name=choice(ascii_uppercase)+choice(ascii_uppercase)+str(choice(range(0,10)))+str(choice(range(0,10)))+str(choice(range(0,10)))
			if new_name not in Robot.names:
				Robot.names.remove(self.name)
				self.name=new_name
				Robot.names.append(new_name)
				name_set=True