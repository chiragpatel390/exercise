from string import ascii_uppercase as UPPER

def make_diamond(letter):
	pattern = []
	for i in range(UPPER.index(letter)+1):
		if i==0:
			pattern.append((UPPER.index(letter)-i)*' '+UPPER[i]+(UPPER.index(letter)-i)*' ')
		else:
			pattern.append((UPPER.index(letter)-i)*' '+UPPER[i]+(i*2-1)*' '+UPPER[i]+(UPPER.index(letter)-i)*' ')

	for i in range(UPPER.index(letter)-1,-1,-1):
		if i==0:
			pattern.append((UPPER.index(letter)-i)*' '+UPPER[i]+(UPPER.index(letter)-i)*' ')
		else:
			pattern.append((UPPER.index(letter)-i)*' '+UPPER[i]+(i*2-1)*' '+UPPER[i]+(UPPER.index(letter)-i)*' ')

	return '\n'.join(pattern)+'\n'


