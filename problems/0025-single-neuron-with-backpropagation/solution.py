import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    updated_weights=initial_weights
    updated_bias=initial_bias
    mse_values=[]
    for ep in range(epochs):
        probabilities=[]
        for feat in range(len(features)):
            add=0
            for weigh in range(len(features[0])):
                add+=features[feat][weigh]*updated_weights[weigh]
            sigmoid=1/(1+np.exp(-(add+updated_bias)))
            probabilities.append(sigmoid)
        mse=0
        for label in range(len(labels)):
            mse+=(probabilities[label]-labels[label])**2
        mse/=len(labels)
        mse_values.append(mse)
        error=probabilities-labels
        loss=2*error*probabilities*(1-np.array(probabilities))
        wGrad=np.dot(features.T,loss)/len(labels)
        bGrad=np.mean(loss)
        updated_weights-=learning_rate*wGrad
        updated_bias-=learning_rate*bGrad
    return updated_weights, updated_bias, mse_values