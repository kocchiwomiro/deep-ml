def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	det=0
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	else:
		row=0
		for column in range(len(matrix)):
			if column%2!=1:
				current=matrix[row][column]
			else:
				current=-matrix[row][column]
			temp=[]
			for i in range(len(matrix)):
				nums=[]
				if i!=row:
					for j in range(len(matrix[0])):
						if j!=column:
							nums.append(matrix[i][j])
					temp.append(nums)
			det+=current*determinant_4x4(temp)
	return det