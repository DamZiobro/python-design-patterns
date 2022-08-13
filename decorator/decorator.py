#! /usr/bin/env python

import time

class ProfilingDecorator():

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self._func(*args, **kwargs) 
        stop_time = time.time()
        print(f"time elapsed: {stop_time - start_time}")


@ProfilingDecorator
def fibonacci(n: int):
    if n < 2:
        return
    fib_prev = 1
    fib = 1

    for n in range(2, n):
        fib_prev, fib = fib, fib + fib_prev

    return fib


if __name__ == "__main__":    
    fib_result = fibonacci(10)
    print(f"fib_result: {fib_result}")
