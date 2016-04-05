import numpy as np

def flip(N):
    """
    Simulates tossing a coin N times, and writes out the number of tails.
    """
    answer = np.random.randint(2, size=N)
    tails = np.where(answer > 0, 0, 1)
    return np.sum(tails)
print flip(100)