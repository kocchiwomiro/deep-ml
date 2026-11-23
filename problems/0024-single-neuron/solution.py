import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities=[]
    for feat in range(len(features)):
        add=0
        for weigh in range(len(features[0])):
            add+=features[feat][weigh]*weights[weigh]
        sigmoid=1/(1+math.exp(-(add+bias)))
        probabilities.append(sigmoid)
    mse=0
    for label in range(len(labels)):
        mse+=(probabilities[label]-labels[label])**2
    mse/=len(labels)
    return probabilities, mse