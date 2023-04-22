import timeit
from numba import cuda
import numpy as np

def secant_method_CPU(a, b, tol):
    f = lambda x: x**2 - 11
    if f(a)*f(b) > 0:
        pass
    else:
        while (b - a) > tol:
            midpoint = a - f(a)*(b-a)/(f(b)-f(a))
            if f(midpoint) == 0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0: 
                b = midpoint
            else:
                a = midpoint
        return(midpoint)
    
@cuda.jit
def secant_method_GPU(a, b, tol, result):
    tid = cuda.threadIdx.x
    f = lambda x: x**2 - 11
    if f(a)*f(b) > 0:
        print("No root found.")
    else:
        while (b - a) > tol:
            midpoint = a - f(a)*(b-a)/(f(b)-f(a))
            if f(midpoint) == 0:
                result[tid]=midpoint 
            elif f(a)*f(midpoint) < 0: 
                b = midpoint
            else:
                a = midpoint
        result[tid]=midpoint

sample = 10000
execution_time = timeit.timeit(lambda:secant_method_CPU(-1, 5, 0.0001), number=sample)
print("Average Time of CPU:", execution_time/sample)

result = cuda.device_array(1, dtype=float)
block_size = 128
grid_size = 512
execution_time = timeit.timeit(lambda:secant_method_GPU[grid_size, block_size](-1, 5, 0.0001,result), number=sample)
print("Average Time of GPU:", execution_time/sample)

'''
timeCPU = 0
for i in range (5): 
    start = timeit.default_timer()
    for i in range (1):
        answer = secant_method_CPU(-1, 5, 0.0001)
    stop = timeit.default_timer()
    timeCPU += stop - start
print('TimeCPU: ',(timeCPU/5))

timeGPU = 0
for i in range (5): 
    start = timeit.default_timer()
    for i in range (1):
        answer = secant_method_GPU(-1, 5, 0.0001)
    stop = timeit.default_timer()
    timeGPU += stop - start
print('TimeGPU: ',(timeGPU/5))
'''