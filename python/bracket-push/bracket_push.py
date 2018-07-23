def is_paired(input_string):
	bracket = {')': '(', '}': '{', ']': '['}

	stack = []
	for i in input_string:
		if i in bracket.values():
			stack.append(i)
		elif i in bracket:
			if not stack:
				return False
			if stack.pop() != bracket[i]:
				return False
	return not stack
