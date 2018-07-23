
def nth_prime(positive_number):
	if positive_number<=0:
		raise ValueError('ValueError')

	prime = []
	i = 2
	while i>1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			prime.append(i)
		i += 1
		if len(prime) >= positive_number:
			break

	return prime[-1]