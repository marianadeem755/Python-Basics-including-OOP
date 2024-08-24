# Function Caching in Python
# Function caching is a technique for improving the performance of a program by storing the results of a function call
#  so that you can reuse the results instead of recomputing them every time the function is called.
# This can be particularly useful when a function is computationally expensive, or when the inputs to the function 
# are unlikely to change frequently.

# In Python, function caching can be achieved using the functools.lru_cache decorator.
#  The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results
#  instead of recomputing them every time the function is called.
#  Here's an example:
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fx(n):
#     if n<2:
#       return n
#     return fx(n-1)+fx(n-2)
# print(fx(20))
# As you can see, the functools.lru_cache decorator is used to cache the results of the fx function. 
# The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None,
#  the cache will have an unlimited size.
# Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a function.
#  With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.

# Conclusion
# Function caching is a technique for improving the performance of a program by storing the results of a function 
# so that you can reuse the results instead of recomputing them every time the function is called.
#  In Python 3, function caching can be achieved using the functools.lru_cache decorator,
#  which provides an easy and efficient way to cache the results of a function. Whether you're writing 
# a computationally expensive program, or just want to simplify your code,
#  function caching is a great technique to have in your toolbox.

import functools
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
print(fx(2))
print(f"Done with 2 with value {fx(2)}")
print(fx(4))
print(f"Done with 4 with value {fx(4)}")
print(fx(6))
print(f"Done with 6 with value {fx(6)}")
print(fx(8))
print(f"Done with 8 with value {fx(8)}")

print(fx(2))
print(f"Done with 2 with value {fx(2)}")
print(fx(4))
print(f"Done with 4 with value {fx(4)}")
print(fx(6))
print(f"Done with 6 with value {fx(6)}")
print(fx(18))
print(f"Done with 18 with value {fx(18)}")
from functools import lru_cache
@lru_cache(maxsize=None)
def fi(n):
    if n==95:
        return n
    return (n-1)+(n-2)
print(fi(118))