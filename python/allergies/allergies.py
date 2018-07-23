class Allergies(object):

	def __init__(self, score):
		self.score=score

	def is_allergic_to(self, item):
		return (item in self.lst)

	@property
	def lst(self):
		l=[]
		temp = self.score%256
		while temp>0:
			if temp >=128:
				l.append("cats")
				temp -= 128
			elif temp >=64:
				l.append("pollen")
				temp -= 64
			elif temp >=32:
				l.append("chocolate")
				temp -= 32
			elif temp >=16:
				l.append("tomatoes")
				temp -= 16
			elif temp >=8:
				l.append("strawberries")
				temp -= 8
			elif temp >=4:
				l.append("shellfish")
				temp -= 4
			elif temp >=2:
				l.append("peanuts")
				temp -= 2
			elif temp ==1:
				l.append("eggs")
				temp -= 1
		return l 