import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x=[]
	for count in range(len(A)):
		x.append(0)
	for count in range(n):
		temp=[]
		for row in range(len(A)):
			summed=0
			for column in range(len(A[0])):
				if row!=column:
					summed+=A[row][column]*x[column]
			temp.append((b[row]-summed)/A[row][row])
		for i in range(len(x)):
			x[i]=temp[i]
	return x