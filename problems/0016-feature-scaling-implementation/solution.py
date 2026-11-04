import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data=data.copy().astype(float)
	normalized_data=data.copy().astype(float)
	for column in range(len(data[0])):
		mean=0
		deviate=0
		mini=data[0][column]
		maxed=data[0][column]
		for row in range(len(data)):
			mean+=data[row][column]
			mini=min(mini,data[row][column])
			maxed=max(maxed,data[row][column])
		mean=mean/len(data)
		for row in range(len(data)):
			deviate+=(data[row][column]-mean)**2
		deviate=(deviate/len(data))**0.5
		for row in range(len(data)):
			standardized_data[row][column]=(data[row][column]-mean)/deviate
			normalized_data[row][column]=(data[row][column]-mini)/(maxed-mini)
	return standardized_data, normalized_data