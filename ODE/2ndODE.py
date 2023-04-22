import timeit
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dydt(u,x,k):
    return [u[1], - k*u[1] - k*u[0] + np.cos(2*x)]

u0 = [0, 0]
t = np.linspace(0,10)

def solve_odeint():
    k = 0.1
    return odeint(dydt, u0, t, args=(k,))

sample=10000
execution_time = timeit.timeit(solve_odeint, number=sample)
print("Degree 1 Average Execution time:", execution_time/sample)

u = solve_odeint()
plt.plot(t, u[:,0], label='u')
plt.plot(t, u[:,1], label='u\'')
plt.xlabel('t')
plt.legend()
plt.show()
