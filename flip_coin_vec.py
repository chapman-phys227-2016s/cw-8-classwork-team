

def flip(N):
    """
    Simulates tossing a coin N times
    """
    answer = numpy.random.randint(2, size=N)
    return answer