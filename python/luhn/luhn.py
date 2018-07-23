class Luhn(object):
	def __init__(self, card_num):
		self.card_num=card_num.replace(' ','')

	def is_valid(self):
		sum = 0
		if self.card_num=='0':
			return False
		elif self.card_num.isdigit():
			for i in range(1,len(self.card_num)+1):
				add=int(self.card_num[-i])*2
				if i%2==0:
					if add>9:
						sum+= add - 9
					else:
						sum += add
				else:
					sum += int(self.card_num[-i])
			if sum%10==0:
				return True
			else:
				return False
		else:
			return False