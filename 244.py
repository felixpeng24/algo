"""
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

"""
#for loop everything? create a list of numbers 100 in length and pop?

from math import sqrt
def sieve(n):
    composite = set()
    for i in range(2, int(sqrt(n))+1):
        for k in range(i, n//i +1):
            composite.add(i*k)
    res = []
    for i in range(2, n+1):
        if i not in composite:
            res.append(i)
    
    return res

from collections import defaultdict
def infinite_sieve():
    def helper(n):
        compositeHash = defaultdict(list)
        for num in range(2, n+1):
            if num not in compositeHash:
                compositeHash[num*num].append(num)
            else:
                for prime in compositeHash[num]:
                    compositeHash[num+prime].extend(compositeHash[num])
        res = set()
        for values in compositeHash.values():
            for value in values:
                res.add(value)

        return list(res)
    n = 2
    primeLen = len(helper(n))
    while True:
        while len(helper(n)) == primeLen:
            n += 1
        primeList = helper(n)
        yield primeList

# print(sieve(100))

g = infinite_sieve()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# def yieldtest():
#     n = 0
#     while True:
#         yield n
#         n +=1


# print(next(yieldtest()))
# print(next(yieldtest()))
# print(next(yieldtest()))
# print(next(yieldtest()))
