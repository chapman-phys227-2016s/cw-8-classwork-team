import numpy as np

def flip(N):
    """
    Simulates tossing a coin N times, and writes out the number of tails.
    """
    return np.random.randint(0, high=2, size=int(N)).sum()

print flip(10)