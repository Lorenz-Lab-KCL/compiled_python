from fib_py import fib_py
from fib_c_annoted import *
import timeit

import sys

# pass in Fib number to calculate
n = int(sys.argv[1])

t1 = min(timeit.repeat(f"fib_py({n})", number=100000, repeat = 10, setup="from fib_py import fib_py; gc.enable()"))
print(f'Pure python: answer = {fib_py(n)}, time = {t1}, speedup = 1.0')

# time each version
t2 = min(timeit.repeat(f"fib_cy_double({n})", number=100000, repeat = 10, setup="from fib_c_annoted import fib_cy_double; gc.enable()"))
print(f'Cython double variables: answer = {fib_cy_double(n)}, time = {t2}, speedup = {t1/t2}')
