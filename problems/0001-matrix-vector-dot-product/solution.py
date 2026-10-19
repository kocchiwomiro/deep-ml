def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	product=[]
	if len(a)!=len(b):
		return -1
	else:
		for row in range(len(a)):
			result=0
			for column in range(len(b)):
				result+=a[row][column]*b[column]
			product.append(result)
	return product