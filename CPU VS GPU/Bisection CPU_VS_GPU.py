import timeit
from numba import cuda
import numpy as np
import math

def bisection_method_CPU(a, b, tol):
    f = lambda x: 2*x-math.cos(x)
    if f(a)*f(b) > 0:
        print("No root found.")
    else:
        while (b - a) >= tol:
            midpoint = (a + b)/2.0
            if f(midpoint) == 0:
                return midpoint
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint
    
@cuda.jit
def bisection_method_GPU(a, b, tol, result):
    tid = cuda.threadIdx.x
    f = lambda x: 2*x-math.cos(x)
    if f(a)*f(b) > 0:
        pass
    else:
        while (b - a) >= tol:
            midpoint = (a + b)/2.0
            if f(midpoint) == 0:
                result[tid] = midpoint
                return
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        result[tid] = midpoint


sample = 10000
execution_time = timeit.timeit(lambda:bisection_method_CPU(-100, 100, 0.0001), number=sample)
print("Average Time of CPU:", execution_time/sample)

result = cuda.device_array(1, dtype=float)
block_size = 128
grid_size = 512
execution_time = timeit.timeit(lambda:bisection_method_GPU[grid_size, block_size](-100, 100, 0.0001, result), number=sample)
print("Average Time of GPU:", execution_time/sample)

'''
for i in range (5): 
    start = timeit.default_timer()
    answer = bisection_method_GPU[grid_size, block_size](-10, 10, 0.0001, d_result)
    stop = timeit.default_timer()
    print('TimeGPU{}:  {}'.format(i+1,(stop - start)))
'''