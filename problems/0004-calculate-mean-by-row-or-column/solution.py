def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	r=len(matrix)
	c=len(matrix[0])
	means=[]
	if(mode=="column"):
		for column in range(c):
			sum=0
			for row in range(r):
				sum+=matrix[row][column]
			means.append(sum/r)
	else:
		for row in range(r):
			sum=0
			for column in range(c):
				sum+=matrix[row][column]
			means.append(sum/c)
	return means