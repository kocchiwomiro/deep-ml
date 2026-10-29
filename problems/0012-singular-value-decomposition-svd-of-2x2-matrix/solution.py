import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    T=np.transpose(A)
    U=np.dot(A, T)
    temp,U=np.linalg.eig(U)
    V=np.dot(T, A)
    S,V=np.linalg.eig(V)
    S=np.flip(np.sort(S))
    for n in range(len(S)):
        S[n]=S[n]**.5
    return U,np.real(S),np.transpose(V)