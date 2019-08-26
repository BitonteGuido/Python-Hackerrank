import numpy

def arrays(arr):
    arr = numpy.array(arr[::-1],float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)