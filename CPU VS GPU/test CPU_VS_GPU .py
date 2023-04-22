import timeit
from numba import cuda
import numpy as np

@cuda.jit
def vector_add_gpu(a, b, result):
    tid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    result[tid] = a[tid] + b[tid]

def vector_add_cpu(a, b):
    return a + b

array_size = 1024 * 1024
a = np.ones(array_size)
b = np.ones(array_size)
result_cpu = np.zeros(array_size)
result_gpu = np.zeros(array_size)

sample = 10000
time_cpu = timeit.timeit(lambda:vector_add_cpu(a, b), number=sample)
print("Average Time of CPU:", time_cpu/sample)

block_size = 128
grid_size = (array_size + (block_size - 1)) // block_size

d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_result = cuda.to_device(result_gpu)

time_gpu = timeit.timeit(lambda:vector_add_gpu[grid_size, block_size](d_a, d_b, d_result), number=sample)
result_gpu = d_result.copy_to_host()

print(" Average Time of GPU:", time_gpu/sample)
