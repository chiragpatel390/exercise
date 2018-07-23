def classify(number):
	if number <= 0:
		raise ValueError("invalid number")
	n = []
	for i in range(1,number):
		if number%i==0:
			n.append(i)
		else:
			continue
	if sum(n) == number:
		return "perfect"
	elif sum(n) > number:
		return "abundant"
	else:
		return "deficient"
