def slices(series, length):
	if length>0 and length<=len(series):
		return [series[i:i + length] for i in range(len(series)-length+1)]
	else:
		raise ValueError("not valid length")
