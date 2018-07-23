from collections import defaultdict

class School(object):
	def __init__(self, name):
		self.name=name
		self.d = defaultdict(set)

	def add(self,name,grade):
		self.d[grade].add(name)
		return self.d.items()

	def grade(self,no):
		return self.d[no]

	def sort(self):
		a = {}
		return sorted((grade, tuple(sorted(students))) for grade, students in self.d.items())
