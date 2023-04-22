import numpy as np
import timeit
import matplotlib.pyplot as plt


x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
y = np.array([3.0, 14.0, 23.0, 25.0, 23.0, 15.0, 9.0, 5.0, 9.0, 13.0, 17.0, 24.0, 32.0, 36.0, 46.0])
nx = np.linspace(min(x), max(x), 100)


def curve(x, y, degree):
    coef = np.polyfit(x, y, degree)
    ny = np.polyval(coef, nx)

    return coef, ny


sample = 10000

execution_time1 = timeit.timeit(lambda: curve(x, y, 1), number=sample)
print("Degree 1 Average Execution time:", execution_time1/sample)

execution_time2 = timeit.timeit(lambda: curve(x, y, 2), number=sample)
print("Degree 2 Average Execution time:", execution_time2/sample)

execution_time3 = timeit.timeit(lambda: curve(x, y, 3), number=sample)
print("Degree 3 Average Execution time:", execution_time3/sample)


plt.plot(x, y, 'o', label='Original data')
coef1, ny1 = curve(x, y, 1)
plt.plot(nx, ny1, label='Degree1')
coef2, ny2 = curve(x, y, 2)
plt.plot(nx, ny2, label='Degree2')
coef3, ny3 = curve(x, y, 3)
plt.plot(nx, ny3, label='Degree3')
plt.legend()
plt.show()