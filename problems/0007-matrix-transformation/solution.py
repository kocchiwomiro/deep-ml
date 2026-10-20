import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if np.linalg.det(T)==0 or np.linalg.det(S)==0:
		return -1
	else:
		transformed_matrix=np.linalg.inv(T)
		transformed_matrix=np.matmul(transformed_matrix, A)
		transformed_matrix=np.matmul(transformed_matrix, S)
	return transformed_matrix