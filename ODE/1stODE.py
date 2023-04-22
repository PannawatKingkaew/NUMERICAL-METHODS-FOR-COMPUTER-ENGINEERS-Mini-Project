import timeit
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dydt(u,x,k):
    return k * np.exp(-x)

y0 = 0
t = np.linspace(0,10,1000)

def solve_odeint():
    k = 0.1
    return odeint(dydt, y0, t, args=(k,))

sample=10000
execution_time = timeit.timeit(solve_odeint, number=sample)
print("Degree 1 Average Execution time:", execution_time/sample)

y = solve_odeint()
plt.plot(t, y, label='y')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
