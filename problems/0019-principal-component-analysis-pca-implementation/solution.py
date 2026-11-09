import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    mean=np.mean(data, axis=0)
    std=np.std(data, axis=0)
    standard=(data-mean)/std
    covar=np.cov(standard, rowvar=False)
    value,vector=np.linalg.eigh(covar)
    index=np.argsort(value)[::-1]
    vector=vector[:,index]
    for i in range(vector.shape[1]):
        if vector[0, i]<0:
            vector[:, i]=-vector[:, i]
    return np.array(vector[:,:k])
