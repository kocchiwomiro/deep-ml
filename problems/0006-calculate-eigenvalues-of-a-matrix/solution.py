def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues=[]
	trace=matrix[0][0]+matrix[1][1]
	det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	sqrt=(trace*trace-4*det)**.5
	eigenvalues.append((trace+sqrt)/2)
	eigenvalues.append((trace-sqrt)/2)
	return eigenvalues