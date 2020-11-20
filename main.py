from functools import lru_cache

@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(10))   # no previously cached result, makes 11 recursive calls
# return 3628800
print(factorial(5))      # just looks up cached value result
# return 120
print(factorial(12))      # makes two new recursive calls, the other 10 are cached
""" 
return 479001600 
"""
print('start... 511')
print(factorial(511))
import time
time.sleep(1)
print('start... 511 again')
print(factorial(511))

# another example
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
print(fib(996)) # fail on more then 997

import sys
sys.setrecursionlimit(2000)
print(fib(1990))