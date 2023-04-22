import timeit

def test(n):
    return sum(range(n))

n = 10000
sample = 10000

execution_time = timeit.timeit(lambda:test(n), number=sample)
print("Average time:", (execution_time / sample),"seconds")
