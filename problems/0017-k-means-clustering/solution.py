def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	final_centroids=initial_centroids.copy()
	for temp in range(max_iterations):
		grouping=[]
		for cent in range(len(final_centroids)):
			grouping.append([])
		for point in range(len(points)):
			first=True
			current=0
			for cent in range(len(final_centroids)):
				dist=0
				for var in range(len(points[0])):
					dist+=(points[point][var]-final_centroids[cent][var])**2
				dist**=0.5
				if first==True:
					current=dist
					close=cent
					first=False
				else:
					if(current<dist):
						current=dist
						close=cent
			grouping[close].append(points[point])
		final_centroids=[]
		for group in range(len(grouping)):
			mean=[]
			for var in range(len(points[0])):
				counter=0
				summed=0
				for point in range(len(grouping[0])):
					counter+=1
					summed+=grouping[group][point][var]
				mean.append(summed/counter)
			final_centroids.append(tuple(mean))
					
	return final_centroids