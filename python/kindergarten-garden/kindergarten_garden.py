class Garden(object):

	def __init__(self, diagram, students='Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry'.split()):
		self.row1,self.row2=diagram.split('\n')
		self.students = sorted(students)


	def plants(self, student):
		code = ''
		code+=self.row1[self.students.index(student)*2] + self.row1[self.students.index(student)*2+1] + self.row2[self.students.index(student)*2] + self.row2[self.students.index(student)*2+1]
		plant_list = []

		for i in code:
			if i=='V':
				plant_list.append('Violets')
			elif i=='R':
				plant_list.append('Radishes')
			elif i=='C':
				plant_list.append('Clover')
			elif i=='G':
				plant_list.append('Grass')

		return plant_list

		