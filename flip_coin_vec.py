import numpy as np

def flip(N):
    """
    Simulates tossing a coin N times, and writes out the number of tails.
    """
    return np.random.randint(2, size=N).sum()