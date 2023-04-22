import timeit
import numba

def bisection_method_CPU(a, b, tol):
    f = lambda x: x**2 - 11
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
    
@numba.njit
def bisection_method_GPU(a, b, tol):
    
    f = lambda x: x**2 - 11
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

sample = 10000
execution_time = timeit.timeit(lambda:bisection_method_CPU(-1, 5, 0.0001), number=sample)
print("Average Time of Source Code:", execution_time/sample)

execution_time = timeit.timeit(lambda:bisection_method_GPU(-1, 5, 0.0001), number=sample)
print("Average Time of Native Code:", execution_time/sample)

'''
for i in range (5): 
    start = timeit.default_timer()
    answer = bisection_method_GPU(-1, 5, 0.0001)
    stop = timeit.default_timer()
    print('TimeNative{}:  {}'.format(i+1,(stop - start)))
'''