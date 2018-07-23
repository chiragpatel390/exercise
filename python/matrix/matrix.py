
class Matrix(object):
	def __init__(self, matrix_string):
		self.m=matrix_string.split('\n')
		self.raw = [[int(i) for i in row.split()]for row in self.m]
		self.columns = [list(i) for i in zip(*self.raw)]


	def row(self, index):
		return self.raw[index]

	def column(self, index):
		return self.columns[index]