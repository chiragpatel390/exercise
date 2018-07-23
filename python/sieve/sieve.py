def sieve(limit):
	p = []
	for i in range(2,limit+1):
		p.append(i)
	for i in range(2,limit+1):
		for j in range(2,limit+1):
			m = i*j
			if m in p:
				p.remove(m)
			else:
				continue
	return p