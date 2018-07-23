def transform(legacy_data):
	dic = {}
	for value, char in legacy_data.items():
		for letter in char:
			dic[letter.lower()]= value
	return dic