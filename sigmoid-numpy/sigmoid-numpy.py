import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_np = np.array(x)
    ex = np.exp(-x_np)
    
    return 1/(1+ex)
   