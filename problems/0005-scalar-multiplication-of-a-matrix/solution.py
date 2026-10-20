def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for row in range(len(matrix)):
		for column in range(len(matrix[0])):
			matrix[row][column]*=scalar
	return matrix