def saddle_points(matrix):
	
	for i in matrix:
		if len(i) != len(matrix[0]):
			raise ValueError('invalid matrix')

	mmax = [max(r) for r in matrix]
	mmin = [min(c) for c in zip(*matrix)]
	points = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if mmax[i] == mmin[j]]
	return set(points)

