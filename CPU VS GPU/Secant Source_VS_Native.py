import timeit
import numba

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
    
@numba.njit
def secant_method_GPU(a, b, tol):
    
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

sample = 10000
execution_time = timeit.timeit(lambda:secant_method_CPU(-1, 5, 0.0001), number=sample)
print("Average Time of CPU:", execution_time/sample)

execution_time = timeit.timeit(lambda:secant_method_GPU(-1, 5, 0.0001), number=sample)
print("Average Time of GPU:", execution_time/sample)

'''
for i in range (5): 
    start = timeit.default_timer()
    answer = bisection_method_CPU(-1, 5, 0.0001)
    stop = timeit.default_timer()
    print('TimeCPU{}:  {}'.format(i+1,(stop - start)))'''