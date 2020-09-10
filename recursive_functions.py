import time
import random

def factorial_recursive(n):
    if n == 1:
            return 1
    else:
            return n * factorial_recursive(n-1)

def infinite_walk_recurse(n):
    print(n)
    time.sleep(2)
    return n + recurse(n + random.randint(-5,5))

def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Better fibonacci recursive
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)