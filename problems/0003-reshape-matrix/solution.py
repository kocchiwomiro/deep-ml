import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	raw=[]
	for row in range(len(a)):
		for column in range(len(a[0])):
			raw.append(a[row][column])
	count=0
	result=[]
	for row in range(new_shape[0]):
		group=[]
		for column in range(new_shape[1]):
			group.append(raw[count])
			count+=1
			if(count>len(raw)):
				return []
		result.append(group)
	if(count<len(raw)):
		return []
	else:
		return result