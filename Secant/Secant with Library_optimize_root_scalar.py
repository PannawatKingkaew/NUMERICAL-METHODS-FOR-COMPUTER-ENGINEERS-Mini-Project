import timeit
from scipy import optimize

fx = lambda x: x**2 - 11

def run_optimize():
    return optimize.root_scalar(fx,x0=-1,x1=5,method='secant', xtol=0.0001)

sample=10000
execution_time = timeit.timeit(run_optimize, number=sample)
print("Average Time:", execution_time/sample)
print("Result:",optimize.root_scalar(fx,x0=-1,x1=5,method='secant', xtol=0.0001))