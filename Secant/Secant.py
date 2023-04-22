import timeit

fx = lambda x: x**2 - 11

def secant_method(f,a, b, tol):

    if f(a)*f(b) > 0:
        print("No root found.")
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
     
sample=10000
execution_time = timeit.timeit(lambda:secant_method(fx,-1, 5, 0.0001), number=10000)
print("Average Time:", execution_time/10000)
print("Result:",secant_method(fx,-1, 5, 0.0001))

