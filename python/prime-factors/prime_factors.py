def prime_factors(natural_number):
	factors = []
	divisor = 2

	while natural_number > 1:
		if natural_number % divisor ==0:
			factors.append(divisor)
			natural_number /= divisor
		else:
			divisor +=1
	return factors