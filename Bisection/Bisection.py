import timeit

fx = lambda x: x**2 - 11

def bisection_method(f,a, b, tol):
    if f(a)*f(b) > 0:
        print("No root found.")
    else:
        while (b - a) >= tol:
            midpoint = (a + b)/2.0
            if f(midpoint) == 0:
                return(midpoint) 
            elif f(a)*f(midpoint) < 0: 
                b = midpoint
            else:
                a = midpoint
        return(midpoint)
    
sample=10000
execution_time = timeit.timeit(lambda:bisection_method(fx,-1, 5, 0.0001), number=sample)

print("Average Time:", execution_time/sample)
print("Result:",bisection_method(fx,-1, 5, 0.0001))
