import numpy as np
from scipy import optimize
import timeit
import matplotlib.pyplot as plt


x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
y = np.array([3.0, 14.0, 23.0, 25.0, 23.0, 15.0, 9.0, 5.0, 9.0, 13.0, 17.0, 24.0, 32.0, 36.0, 46.0])
nx = np.linspace(min(x), max(x), 100)


def degree3(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def degree2(x, a, b, c):
    return a*x**2 + b*x + c

def degree1(x, a, b):
    return a*x + b


def run_code3():
    popt, pcov = optimize.curve_fit(degree3, x, y)
    ny = degree3(nx, *popt)
    return popt, ny

def run_code2():
    popt, pcov = optimize.curve_fit(degree2, x, y)
    ny = degree2(nx, *popt)
    return popt, ny

def run_code1():
    popt, pcov = optimize.curve_fit(degree1, x, y)
    ny = degree1(nx, *popt)
    return popt, ny

sample = 10000
execution_time1 = timeit.timeit(run_code1, number=sample)
execution_time2 = timeit.timeit(run_code2, number=sample)
execution_time3 = timeit.timeit(run_code3, number=sample)

print("Degree 1 Average Execution time:", execution_time1/sample)
print("Degree 2 Average Execution time:", execution_time2/sample)
print("Degree 3 Average Execution time:", execution_time3/sample)


# Plot the results
plt.plot(x, y, 'o', label='Original data')
popt1, ny1 = run_code1()
plt.plot(nx, ny1, label='Degree1')
popt2, ny2 = run_code2()
plt.plot(nx, ny2, label='Degree2')
popt3, ny3 = run_code3()
plt.plot(nx, ny3, label='Degree3')
plt.legend()
plt.show()
