from math import sqrt
from math import gcd

def primitive_triplets(number_in_triplet):
	if number_in_triplet % 4 != 0:
		raise ValueError('Argument must be divisible by 4')
	t = []
	r = number_in_triplet * number_in_triplet//4
	for i in range(2, number_in_triplet+1):
		k = i*i + number_in_triplet**2
		if sqrt(k) == int(sqrt(k)):
			if gcd(i, number_in_triplet)==1:
				if gcd(number_in_triplet, int(sqrt(k)))==1:
					if gcd(i, int(sqrt(k)))==1:
						t.append(tuple(sorted([i, number_in_triplet, int(sqrt(k))])))
	for i in range(number_in_triplet, r):
		k = number_in_triplet**2 + i*i
		if sqrt(k) == int(sqrt(k)):
			if gcd(i, number_in_triplet)==1:
				if gcd(number_in_triplet, int(sqrt(k)))==1:
					if gcd(i, int(sqrt(k)))==1:
						t.append(tuple(sorted([number_in_triplet, i, int(sqrt(k))])))

	return set(t)


def triplets_in_range(range_start, range_end):
	t = []
	for i in range(range_start, range_end+1):
		for j in range(i+1, range_end+1):
			k = i*i + j*j
			if sqrt(k) in range(range_start, range_end+1):
				t.append((i, j, sqrt(k)))

	return set(t)


def is_triplet(triplet):
	t = list(triplet)
	t.sort()
	return t[0] * t[0] + t[1] * t[1] == t[2] * t[2]
