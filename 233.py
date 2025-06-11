"""
This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

"""

#we only need the last two numbers as a cache

def fib(n):
    if n == 1 or n == 2:
        return 1
    cache1 = 1
    cache2 = 1

    for _ in range(2, n):
        cache2, cache1 = cache1+cache2, cache2
    
    return cache2

for num in range(1, 12):
    print(fib(num))