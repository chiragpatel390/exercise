def largest_palindrome(max_factor, min_factor):
	products={}
	for i in range (min_factor,max_factor+1):
		for j in range(i,max_factor+1):
			product=i*j
			if str(product)==str(product)[::-1]:
				if product in products.keys():
					factors=products[product]
					factors.append((i,j))
					products[product]=factors
				else:
					products[product]=[(i,j)]

	largest_palindrome=max(products.keys())
	factors=set(products[largest_palindrome])

	return largest_palindrome,set(products[largest_palindrome])


def smallest_palindrome(max_factor, min_factor):
	smallest_palindrome=None
	for i in range(min_factor,max_factor+1):
		for j in range(i,max_factor+1):
			product=i*j
			if str(product)==str(product)[::-1]:
				smallest_palindrome=product
				factors={(i,j)}
				break
		if type(smallest_palindrome) is int:
			break
	if smallest_palindrome is None:
		raise ValueError('ValueError`')
	return smallest_palindrome,factors
