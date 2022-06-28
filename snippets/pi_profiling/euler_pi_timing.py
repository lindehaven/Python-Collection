import time
import euler_pi

if __name__ == '__main__':
    t0 = time.perf_counter()
    euler_pi.euler_pi(6)
    t1 = time.perf_counter()
    print('Function call took', t1-t0, 'seconds.')
