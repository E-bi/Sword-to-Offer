#方法1：
import time

def fib_fir(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fir(n-1)+fib_fir(n-2)
    
#方法2

def fib_sec(n):
    
    if n <= 0:
        return 0 
    elif n==1:
        return 1
    elif n == 2:
        return 1
    else:
        fib0 = 0
        fib1 = 1
        for i in range(n-2):
            fib2 = fib0 + fib1
            fib0 = fib1
            fib1 = fib2
        return fib2
