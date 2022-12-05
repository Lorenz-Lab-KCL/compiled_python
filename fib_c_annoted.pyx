def fib_cy_double(int n):
    cdef double a = 0.
    cdef double b = 1.
    cdef int i
    for i in range(n - 1):
        a, b = a + b, a
    return a
