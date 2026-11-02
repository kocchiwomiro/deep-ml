import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	T=np.transpose(X)
	first=np.dot(T,X)
	second=np.linalg.inv(first)
	third=np.dot(second,T)
	theta=np.dot(third,y)
	return theta