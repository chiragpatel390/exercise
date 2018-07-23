def abbreviate(words):
	words=words.replace(',','')
	words=words.replace('-',' ')
	l = words.split(' ')
	a = ''
	for i in l:
		a += i[0].upper()
	return a