def arrays(arr):
    arr = [float(x) for x in arr]
    arr.reverse()
    return numpy.array(arr, float)
