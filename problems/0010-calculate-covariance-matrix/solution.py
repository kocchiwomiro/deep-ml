def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	means=[]
	for row in range(len(vectors)):
		summed=0
		for column in range(len(vectors[0])):
			summed+=vectors[row][column]
		means.append(summed/len(vectors[0]))
	result=[]
	for row1 in range(len(vectors)):
		x=[]
		for row2 in range(len(vectors)):
			summed=0
			for column in range(len(vectors[0])):
				summed+=(vectors[row1][column]-means[row1])*(vectors[row2][column]-means[row2])
			x.append(summed/(len(vectors[0])-1))
		result.append(x)
	return result