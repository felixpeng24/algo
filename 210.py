"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?


easy

"""

def collatz(num):
    if num == 1:
        return True
    elif num % 2 == 1:
        return collatz((3*num)+1)
    else:
        return collatz(num / 2)
    