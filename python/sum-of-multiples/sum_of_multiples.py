
def sum_of_multiples(limit, multiples):
	a=[]
	for i in multiples:
		for j in range(1,limit):
			if i*j<limit:
				a.append(i*j)
	return sum(set(a))