SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def check_lists(first_list, second_list):
	if first_list == second_list:
		return EQUAL

	elif len(first_list) < len(second_list):
		if len(first_list) == 0:
			return SUBLIST
		for i in range(len(second_list)):
			if first_list[0] == second_list[i]:
				if first_list == second_list[i:i+len(first_list)]:
					return SUBLIST

	elif len(first_list) > len(second_list):
		if len(second_list) == 0:
			return SUPERLIST
		for i in range(len(first_list)):
			if second_list[0] == first_list[i]:
				if second_list == first_list[i:i+len(second_list)]:
					return SUPERLIST

	return UNEQUAL
