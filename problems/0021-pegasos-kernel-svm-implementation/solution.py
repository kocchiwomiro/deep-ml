import numpy as np

def pegasos_kernel_svm(data: np.ndarray, labels: np.ndarray, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0) -> tuple:
    """
    Train a kernel SVM using the deterministic Pegasos algorithm.
    
    Args:
        data: Training data of shape (n_samples, n_features)
        labels: Labels of shape (n_samples,) with values in {-1, 1}
        kernel: 'linear' or 'rbf'
        lambda_val: Regularization parameter
        iterations: Number of training iterations
        sigma: RBF kernel bandwidth (only used if kernel='rbf')
    
    Returns:
        Tuple of (alphas, bias) where alphas is a list and bias is a float
    """
    alphas=np.zeros(len(data))
    bias=0
    for iter in range(1,iterations+1,1):
        n=1/(lambda_val*iter)
        for sample in range(len(data)):
            g=0
            for l in range(len(labels)):
                if kernel=='linear':
                    k=np.dot(data[l],data[sample])
                elif kernel=='rbf':
                    k=np.exp(-np.sum((data[l]-data[sample])**2)/(2*sigma**2))
                g+=alphas[l]*labels[l]*k
            g+=bias
            if g*labels[sample]<1:
                alphas[sample]+=n*(1-lambda_val*alphas[sample])
                bias+=n*labels[sample]
            else:
                alphas[sample]-=n*lambda_val*alphas[sample]
    return tuple([alphas,bias])