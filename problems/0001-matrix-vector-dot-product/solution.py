def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	res = [0 * len(b) for _ in range(len(a))]
	for i in range(len(a)):
		for k in range(len(b)):
			res[i] += a[i][k] * b[k]

	return res
	
	
	