import numpy

def arrays(arr):
    arr = list(map(float, arr))
    
    a = numpy.array(arr)
    
    filtered_reversed = a[::-1]
    
    return filtered_reversed

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
