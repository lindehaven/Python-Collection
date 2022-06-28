from time import perf_counter

ITERATIONS = 100_000_000

def function_to_time(arg):
    for _ in range(arg):
        pass

if __name__ == '__main__':
    t0 = perf_counter()
    function_to_time(ITERATIONS)
    t1 = perf_counter()
    print(ITERATIONS, 'iterations took', t1-t0, 'seconds.')
