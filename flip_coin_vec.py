

def flip(N):
    """
    Simulates tossing a coin N times, and writes out the number of tails.
    """
    answer = numpy.random.randint(2, size=N)
    tails = numpy.where(answer>= 0.5 , 0, 1)
    return tails